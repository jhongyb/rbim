from django.shortcuts import render
from django.utils import timezone
from inhabitants.models import Inhabitants
from datetime import date
from django.db.models import Case, IntegerField, Q, Value, When,Count,CharField
from django.db.models.functions import ExtractYear

def population_by_sex(request,pk):
    # Fetch all inhabitants with sex and birthday recorded
    inhabitants = Inhabitants.objects.filter(birthday__isnull=False, sex__isnull=False,hh__barangay__name=pk).select_related('sex')
    
    # Initialize the 5-year buckets matching the image layout
    age_groups = [
        '0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39',
        '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85+'
    ]
    
    # Setup data counters
    # Note: Use whatever string representations your Sex model uses (e.g., 'Male'/'Female' or 'M'/'F')
    male_counts = {group: 0 for group in age_groups}
    female_counts = {group: 0 for group in age_groups}
    
    today = date.today()
    total_population = 0

    for person in inhabitants:
        # Calculate dynamic age
        dob = person.birthday
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        # Determine age bucket string
        if age >= 85:
            bucket = '85+'
        else:
            lower = (age // 5) * 5
            upper = lower + 4
            bucket = f"{lower}-{upper}"
            
        # Standardize sex identifier based on your foreign key string mapping
        if hasattr(person.sex, 'description') and person.sex.description:
            sex_str = person.sex.description.strip().upper()
        else:
            sex_str = str(person.sex).upper()
        
        # FIX: Match the exact string value instead of using 'in'
        if sex_str == 'MALE':
            male_counts[bucket] += 1
            total_population += 1
        elif sex_str == 'FEMALE':
            female_counts[bucket] += 1
            total_population += 1

    # Convert counts to percentages (and make males negative for the left side of the chart)
    male_percentages = []
    female_percentages = []
    
    for group in age_groups:
        if total_population > 0:
            m_pct = (male_counts[group] / total_population) * 100
            f_pct = (female_counts[group] / total_population) * 100
        else:
            m_pct, f_pct = 0, 0
            
        # Male values MUST be negative to render on the left side of the pyramid base
        male_percentages.append(-abs(m_pct))
        female_percentages.append(f_pct)

    context = {
        'age_groups': age_groups,
        'male_data': male_percentages,
        'female_data': female_percentages,
        'brgy':pk
    }
    
    return render(request, 'rbim/popbysex.html', context)

def population_by_civilstatus(request,pk):
    status_query = Inhabitants.objects.values('maritalstatus__description')\
                                      .annotate(total=Count('id'))\
                                      .order_by('maritalstatus__description').filter(hh__barangay__name=pk)
    civil_labels = []
    civil_values = []
    
    for entry in status_query:
        label = entry['maritalstatus__description']
        label = str(label).upper() if label else "UNKNOWN"
        civil_labels.append(label)
        civil_values.append(entry['total'])

    context = {
        'civil_labels': civil_labels,
        'civil_values': civil_values,
        'brgy':pk
    }
    return render(request, 'rbim/popbycivilstatus.html', context)

def population_by_religion(request,pk):
    status_query = Inhabitants.objects.values('religion__description')\
                                      .annotate(total=Count('id'))\
                                      .order_by('religion__description').filter(hh__barangay__name=pk)
    rel_labels = []
    rel_values = []

    for entry in status_query:
        label = entry['religion__description']
        label = str(label).upper() if label else "UNKNOWN"
        rel_labels.append(label)
        rel_values.append(entry['total'])

    context = {
        'rel_labels': rel_labels,
        'rel_values': rel_values,
        'brgy':pk
    }
    return render(request, 'rbim/popbyreligion.html', context)

def population_by_ethnicity(request,pk):
    status_query = Inhabitants.objects.values('etnicity__description')\
                                      .annotate(total=Count('id'))\
                                      .order_by('etnicity__description').filter(hh__barangay__name=pk)
    eth_labels = []
    eth_values = []

    for entry in status_query:
        label = entry['etnicity__description']
        label = str(label).upper() if label else "UNKNOWN"
        eth_labels.append(label)
        eth_values.append(entry['total'])
    context = {
        'rel_labels': eth_labels,
        'rel_values': eth_values,
        'brgy':pk
    }
    return render(request, 'rbim/popbyethnic.html', context)

def population_by_nationality(request,pk):
    status_query = Inhabitants.objects.values('nationality__description')\
                                          .annotate(total=Count('id'))\
                                          .order_by('nationality__description').filter(hh__barangay__name=pk)
    nat_labels = []
    nat_values = []
    for entry in status_query:
            label = entry['nationality__description']
            label = str(label).upper() if label else "UNKNOWN"
            nat_labels.append(label)
            nat_values.append(entry['total'])
    context = {
            'nat_labels': nat_labels,
            'nat_values': nat_values,
            'brgy':pk
        }
    return render(request, 'rbim/popbynationality.html', context)


def population_by_higheducation(request, pk):
    # 1. Filter inhabitants for the specific barangay AND age >= 5
    current_year = date.today().year

    # 1. Query inhabitants & calculate age from birthday
    # Filters out null birthdays and age < 5
    queryset = (
        Inhabitants.objects.filter(
            hh__barangay__name=pk, birthday__isnull=False
        )
        .annotate(calculated_age=Value(current_year) - ExtractYear("birthday"))
        .filter(calculated_age__gte=5)
    )

    # 2. Annotate age brackets matching the image layout (55-69 is grouped)
    queryset = queryset.annotate(
        age_group=Case(
            When(calculated_age__range=(5, 9), then=Value("05-09")),
            When(calculated_age__range=(10, 14), then=Value("10-14")),
            When(calculated_age__range=(15, 19), then=Value("15-19")),
            When(calculated_age__range=(20, 24), then=Value("20-24")),
            When(calculated_age__range=(25, 29), then=Value("25-29")),
            When(calculated_age__range=(30, 34), then=Value("30-34")),
            When(calculated_age__range=(35, 39), then=Value("35-39")),
            When(calculated_age__range=(40, 44), then=Value("40-44")),
            When(calculated_age__range=(45, 49), then=Value("45-49")),
            When(calculated_age__range=(50, 54), then=Value("50-54")),
            When(
                calculated_age__range=(55, 69), then=Value("55-69")
            ),  # Matches the chart grouping
            When(calculated_age__range=(70, 74), then=Value("70-74")),
            When(calculated_age__range=(75, 79), then=Value("75-79")),
            When(calculated_age__range=(80, 84), then=Value("80-84")),
            When(calculated_age__gte=85, then=Value("85+")),
            default=Value("UNKNOWN"),
            output_field=CharField(),
        )
    )

    # 3. Aggregation grouped by Education Level & Age Group
    status_query = (
        queryset.values("highesteducation__description", "age_group")
        .annotate(total=Count("id"))
        .order_by("highesteducation__description", "age_group")
    )

    # 4. Extract distinct education labels for chart X-Axis
    raw_labels = queryset.values_list(
        "highesteducation__description", flat=True
    ).distinct()

    education_labels = [
        str(label).upper() if label else "UNKNOWN" for label in raw_labels
    ]

    # Pre-defined ordered age brackets to keep matrix consistent
    ordered_age_groups = [
        "05-09",
        "10-14",
        "15-19",
        "20-24",
        "25-29",
        "30-34",
        "35-39",
        "40-44",
        "45-49",
        "50-54",
        "55-69",
        "70-74",
        "75-79",
        "80-84",
        "85+",
    ]

    # Initialize data matrix with zeros for every label/age combination
    data_by_age = {
        group: {edu: 0 for edu in education_labels}
        for group in ordered_age_groups
    }

    # Populate actual aggregated counts
    for entry in status_query:
        edu = (
            str(entry["highesteducation__description"]).upper()
            if entry["highesteducation__description"]
            else "UNKNOWN"
        )
        age_grp = entry["age_group"]
        count = entry["total"]

        if age_grp in data_by_age and edu in data_by_age[age_grp]:
            data_by_age[age_grp][edu] = count

    context = {
        "edu_labels": education_labels,
        "age_datasets": data_by_age,
        "brgy": pk,
    }

    return render(request, "rbim/popbyhigheducation.html", context)
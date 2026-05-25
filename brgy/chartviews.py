from django.shortcuts import render
from django.utils import timezone
from inhabitants.models import Inhabitants
from datetime import date
from django.db.models import Count

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
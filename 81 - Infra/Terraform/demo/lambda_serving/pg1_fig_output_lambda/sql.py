
group_rating_sql = '''
    SELECT 
        review_date, 
        AVG(overall_rating) as overall,
        AVG(culture_and_values) as culture_and_values,
        AVG(work_life_balance) as work_life_balance,
        AVG(senior_management) as senior_management,
        AVG(compensation_and_benefits) as compensation_and_benefits,
        AVG(career_opportunities) as career_opportunities
    FROM main_db
    WHERE "brand" ~ '{brand}'
        AND "review_date" >= '{start_date}'
        AND "review_date" < '{end_date}'
    GROUP BY brand, review_date
    ORDER BY review_date DESC NULLS LAST 
    '''

year_band_sql = '''
    SELECT 
        t.range AS years_at_company, 
        job_status, 
        AVG(overall_rating) as overall_rating,
        COUNT(external_id) as count
    from (
        SELECT external_id, brand, review_date, years_at_company, job_status, overall_rating,
            CASE  
                WHEN years_at_company between 0 and 1 THEN '0-1 year(s)'
                WHEN years_at_company between 2 and 4 THEN '2-4 years'
                WHEN years_at_company between 5 and 10 THEN '5-10 years'
                ELSE '11-99'  
            END AS range
        FROM main_db
        WHERE "brand" ~ '{brand}'
            AND "review_date" >= '{start_date}'
            AND "review_date" < '{end_date}'
    ) t
    GROUP BY t.range, job_status
'''
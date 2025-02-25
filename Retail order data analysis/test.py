import streamlit as st
import pandas as pd
import pymysql 


# Page Config
st.set_page_config(page_title="Retail Order Data Analysis", layout="wide")

# Custom CSS for Heading
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap');

    /* Apply Sky-Themed Background */
    .main {
        background: linear-gradient(to bottom, #87CEEB, #E0FFFF); /* Light Sky Blue to Pale Blue */
        background-attachment: fixed;
        padding: 20px;
        height: 100vh;
    }
    
    .title {
        text-align: center;
        font-size: 60px;
        font-family: 'monotype corsiva';
        background: linear-gradient(to right, blue, red);
        -webkit-background-clip: text;
        color: transparent;
        text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.4);
    }


    /* Button Styling */
    div.stButton > button {
        width: 100%;
        background-color: #ffcccc !important; /* Light Red */
        color: black !important;
        border: 2px solid red !important;
        border-radius: 8px;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease-in-out;
    }

    /* Button Hover Effect */
    div.stButton > button:hover {
        background-color: #ccffcc !important; /* Light Green */
        border: 2px solid lightgreen !important;
        color: black !important;
        box-shadow: 0px 0px 15px rgba(144, 238, 144, 0.9); /* Neon glow effect */
        transform: scale(1.1); /* Slightly increases size */
        font-size: 20px; /* Increases text size */
        transition: all 0.3s ease-in-out;
    }

    </style>

    <h1 class="title">Retail Order Data Analysis</h1>
""", unsafe_allow_html=True)

# Database connection
myconnection = pymysql.connect(host='127.0.0.1', user='root', passwd='Admin@123', database="retail_order")
cursor = myconnection.cursor()

# Layout with equal button size
col1, col2 = st.columns(2)

with col1:
    if st.button("Q1. Find top 10 highest revenue generating products"):
        cursor.execute(""" SELECT sub_category, round(SUM(sale_price),2) AS total_revenue
        FROM sales_table
        GROUP BY sub_category  
        ORDER BY total_revenue DESC
        LIMIT 10;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col1:
    if st.button("Q2. Find the top 5 cities with the highest profit margins"):
        cursor.execute(""" SELECT ot.city, ROUND(SUM(st.total_profit)) AS t_profit
        FROM order_table AS ot
        JOIN sales_table AS st ON ot.order_id = st.order_id
        GROUP BY ot.city
        ORDER BY t_profit DESC
        LIMIT 5;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col1:
    if st.button("Q3. Calculate the total discount given for each category"):
        cursor.execute(""" SELECT category, ROUND(SUM(discount),2) 
        FROM sales_table 
        GROUP BY category;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col1:
    if st.button("Q4. Find the average sale price per product category"):
        cursor.execute(""" SELECT sub_category, ROUND(AVG(sale_price), 2) 
        FROM sales_table 
        GROUP BY sub_category;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col1:
    if st.button("Q5. Find the region with the highest average sale price"):
        cursor.execute(""" select ot.region , round(avg(st.sale_price)) as sales_avg
        from order_table as ot
        join sales_table as st on ot.order_id = st.order_id
        group by ot.region
        order by sales_avg desc
        limit 5;
        """)
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col1:
    if st.button("Q6. Find the total profit per category"):
        cursor.execute(""" select category , round(sum(total_profit),2)
from sales_table
group by category;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col1:
    if st.button("Q7. Identify the top 3 segments with the highest quantity of orders"):
        cursor.execute(""" select ot.segment, sum(st.quantity) as quantity
from order_table as ot
join sales_table as st on ot.order_id = st.order_id
group by ot.segment
order by quantity desc;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col1:
    if st.button("Q8. Determine the average discount percentage given per region"):
        cursor.execute(""" select ot.region , concat(round(avg(st.discount),2),'%') as average_discount
from order_table as ot
join sales_table as st on st.order_id = ot.order_id
group by ot.region;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col1:
    if st.button("Q9. Find the product category with the highest total profit"):
        cursor.execute(""" select sub_category , round(sum(total_profit),2) as total_profit
from sales_table
group by sub_category
order by total_profit desc;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col1:
    if st.button("Q10. Calculate the total revenue generated per year"):
        cursor.execute(""" select year(ot.order_date) as year, round(sum(st.total_profit),2) as total_revenue
from order_table as ot
join sales_table as st on ot.order_id = st.order_id
group by year(ot.order_date);""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col2:
    if st.button("Q11. Which region received the highest discount?"):
        cursor.execute(""" select ot.region, round(sum(st.discount)) as discount
from order_table as ot
join sales_table as st on ot.order_id  = st.order_id
group by ot.region
order by discount desc
limit 1;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col2:
    if st.button("Q12. Which city has the highest sales?"):
        cursor.execute(""" select ot.city , round(sum(st.sale_price)) as sale
from order_table as ot
join sales_table as st on ot.order_id = st.order_id
group by ot.city
order by sale desc
limit 1;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col2:
    if st.button("Q13. Which segment has the lowest quantity of orders?"):
        cursor.execute(""" select ot.segment, round(sum(st.quantity)) as quantity
from order_table as ot
join sales_table as st on ot.order_id = st.order_id
group by ot.segment
order by quantity asc
limit 1;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col2:
    if st.button("Q14. Which five states have the lowest profit?"):
        cursor.execute(""" select  ot.state, round(sum(st.total_profit)) as profit
from order_table as ot
join sales_table as st on st.order_id = ot.order_id
group by ot.state
order by profit asc
limit 5;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col2:
    if st.button("Q15. Which segment is generating the lowest revenue?"):
        cursor.execute(""" select ot.segment, round(sum(st.total_profit)) as revenue
from order_table as ot
join sales_table as st on ot.order_id = st.order_id
group by ot.segment
order by revenue asc
limit 1;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col2:
    if st.button("Q16. What is the profit for each region?"):
        cursor.execute(""" select ot.region, round(sum(st.total_profit))
from order_table as ot
join sales_table as st on ot.order_id = st.order_id
group by ot.region;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col2:
    if st.button("Q17. Which cities have a discount of more than 5%?"):
        cursor.execute(""" select ot.city , st.quantity
from order_table as ot
join sales_table as st on ot.order_id = st.sales_id
where st.quantity > 5;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col2:
    if st.button("Q18. What products are sold in the South region?"):
        cursor.execute(""" select ot.region,st.sub_category
from order_table as ot
join sales_table as st on ot.order_id = st.order_id
where ot.region  = "south"
group by st.sub_category;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col2:
    if st.button("Q19. Which region has the highest quantity of phone sales?"):
        cursor.execute(""" select ot.region, round(sum(st.quantity)) as quantity
from order_table as ot
join sales_table as st on ot.order_id = st.order_id
where st.sub_category = "phones"
group by ot.region
order by quantity desc;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)

with col2:
    if st.button("Q20. Which product generates the highest profit in Florida?"):
        cursor.execute(""" select ot.state, st.sub_category as product, round(sum(st.total_profit)) as profit
from order_table as ot
join sales_table as st on ot.order_id = st.order_id
where ot.state = "Florida"
group by product
order by profit desc;""")
        result = cursor.fetchall()
        col_name = [i[0] for i in cursor.description]
        df = pd.DataFrame(result, columns=col_name)
        st.dataframe(df)
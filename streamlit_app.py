# Import python packages
import streamlit as st


from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want to Custom Smoothie!
    """
)

import streamlit as st

name_on_order = st.text_input('name on smoothie:')
st.write('The name on your smoothie will be', name_on_order)


cnx=st.connection("snowflake")
session =cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

 



ingredients_list = st.multiselect(
     'choose up to 5 ingrdients',
    my_dataframe,
    max_selections=5
)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string=''
    for fruit_choosen in ingredients_list:
        ingredients_string += fruit_choosen +' '
    st.text(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""

    #st.write(my_insert_stmt)
    #st.stop()
    time_to_insert=st.button('submit order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)


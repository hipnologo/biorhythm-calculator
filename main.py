import streamlit as st
import datetime
import math
import matplotlib.pyplot as plt

def calculate_biorhythm(birth_date, target_date, cycle):
    diff = target_date - birth_date
    days = diff.days
    return math.sin(2*math.pi*(days%cycle)/cycle)

def get_biorhythms(birth_date, target_date):
    biorhythms = {
        'Physical': calculate_biorhythm(birth_date, target_date, 23),
        'Emotional': calculate_biorhythm(birth_date, target_date, 28),
        'Intellectual': calculate_biorhythm(birth_date, target_date, 33)
    }
    return biorhythms

def main():
    st.title("Biorhythm Calculator")
    
    birth_date = st.date_input("Enter your birth date")
    target_date = st.date_input("Enter the target date")
    
    if st.button("Calculate Biorhythms"):
        st.write("Calculating biorhythms for the dates 2 days before and 32 days after the target date...")
        results = []
        dates = []
        physical = []
        emotional = []
        intellectual = []
        for i in range(-2, 33):
            date = target_date + datetime.timedelta(days=i)
            biorhythms = get_biorhythms(birth_date, date)
            results.append([date, biorhythms['Physical'], biorhythms['Emotional'], biorhythms['Intellectual']])
            dates.append(date)
            physical.append(biorhythms['Physical'])
            emotional.append(biorhythms['Emotional'])
            intellectual.append(biorhythms['Intellectual'])
        
        st.write("Date, Physical, Emotional, Intellectual")
            
        plt.figure(figsize=(10,5))
        plt.plot(dates, physical, label='Physical')
        plt.plot(dates, emotional, label='Emotional')
        plt.plot(dates, intellectual, label='Intellectual')
        plt.xlabel('Date')
        plt.ylabel('Biorhythm')
        plt.title('Biorhythm Cycles')
        plt.grid(True)
        plt.legend()
        st.pyplot(plt.gcf())

#	for result in results:
#	    st.markdown(f"{result[0]:%Y-%m-%d}, {result[1]:.2f}, {result[2]:.2f}, {result[3]:.2f}$

if __name__ == "__main__":
    main()


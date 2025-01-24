import streamlit as st

# Custom CSS for better styling
st.markdown("""
<style>
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #2E86C1;
    }
    .stMarkdown ul {
        list-style-type: square;
        padding-left: 20px;
    }
    .stMarkdown li {
        margin-bottom: 10px;
    }
    .stButton button {
        background-color: #28B463;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton button:hover {
        background-color: #239B56;
    }
    /* Style for the top navigation menu */
    .top-nav {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
        padding: 10px 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
    }
    .top-nav button {
        background: none;
        border: none;
        color: #2E86C1;
        font-size: 16px;
        cursor: pointer;
        padding: 10px 15px;
        flex: 1;
        text-align: center;
        margin: 0 5px;
        border-radius: 5px;
        transition: background-color 0.3s, color 0.3s;
    }
    .top-nav button:hover {
        background-color: #239B56;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Function to update the page
def update_page(page_name):
    st.session_state.page = page_name

# Function for Home Page
def home_page():
    st.title("🏙️ Woven City: Toyota's Futuristic City")
    st.subheader("A Living Laboratory for the Future of Urban Living")

    # Image (Replace with actual image path)
    try:
        st.image("woven_city_image.jpg", caption="Artist's rendering of Woven City", use_container_width=True)
    except FileNotFoundError:
        st.image("https://via.placeholder.com/800x400.png?text=Woven+City+Image+Not+Found", caption="Placeholder Image", use_container_width=True)

    st.markdown("---")
    st.write("Welcome to the Woven City Explorer!")
    st.markdown("""
      Woven City is a project developed by Toyota, which began its construction in 2021. The project is still in its early stages, and the first phase of construction was completed in 2023. This initial phase laid the groundwork for the city’s infrastructure, including roads, utilities, and basic facilities.

      The city began accepting its first residents in early 2024 as part of a pilot program with around 100 residents. These initial residents are key to testing and refining the technologies integrated into the city, such as autonomous vehicles, robotics, and AI-driven systems. The population is expected to grow gradually, with a projected total population of approximately 2,000 residents in the coming years as more phases of the city’s development are completed.

       Woven City is designed as a living laboratory where technology, sustainability, and urban innovation can be tested in real-world conditions. The city will continue evolving over time, integrating new technologies and expanding its facilities.
    """)

# Function for "What is Woven City?" Page
def what_is_woven_city():
    st.header("❓ What is Woven City?")
    st.markdown("""
    - **A futuristic city** being developed by Toyota in Japan.
    - Designed to be a **living laboratory** for testing and developing cutting-edge technologies.
    - Focus on **autonomous vehicles**, **artificial intelligence**, **robotics**, and **sustainable living**.
    - Located at the foot of **Mount Fuji**, on the site of a former Toyota factory.
    """)

# Function for "Key Features" Page
def key_features():
    st.header("🌟 Key Features of Woven City")
    st.markdown("""
    - **Autonomous Vehicles:** Dedicated lanes for self-driving cars and robots.
    - **Smart Homes:** Equipped with advanced technology for energy efficiency, security, and personalized comfort.
    - **Three Distinct Zones:**
        - Pedestrian zones 🚶‍♂️
        - Lanes for autonomous vehicles 🚗
        - Routes for active transportation like bicycles 🚴‍♀️.
    - **Sustainable Living:** Utilizing renewable energy sources and incorporating sustainable building practices.
    - **Community Focus:** Designed to foster a strong sense of community among residents.
    - **Disaster Resilience**: Earthquake-resistant structures and redundant energy systems.
    - **Living Laboratory**: A real-world testbed for mobility, robotics, and sustainability innovations.
    - **Seamless Connectivity**: 5G-enabled infrastructure with real-time data collection and AI optimization.
    - **Green Urban Design**: Parks, gardens, and walkable spaces for enhanced well-being.
                
    """)

# Function for "Technology Focus" Page
def technology_focus():
    st.header("🔧 Choose a Technology Focus")
    tech_focus = st.selectbox(
        "Select a key technology:",
        ["Autonomous Vehicles", "Artificial Intelligence", "Robotics", "Sustainability"]
    )

    if tech_focus == "Autonomous Vehicles":
        st.write("**🚗 Autonomous Vehicles:**")
        st.markdown("""
        Woven City will feature a comprehensive network of roads for autonomous vehicles. 
        Residents can seamlessly travel within the city using self-driving cars and robots. 
        This will improve safety, reduce traffic congestion, and enhance accessibility for all.

        - **Dedicated Network of Roads:** Separate pathways for autonomous vehicles ensure safe and efficient traffic flow without interference from pedestrians or cyclists.
        - **Toyota e-Palette Shuttles:** Self-driving electric vehicles will serve as the backbone of transportation, supporting commuting, goods delivery, and multifunctional roles such as mobile shops or clinics.
        - **On-Demand Mobility:** Residents can use an app-based system to call autonomous vehicles, enabling convenient, personalized, and shared transportation.
        - **Enhanced Safety:** Equipped with AI and advanced sensors, these vehicles will minimize accidents and optimize traffic patterns.
        - **Reduced Traffic Congestion:** Coordinated movement of autonomous vehicles will streamline traffic flow, eliminate unnecessary idling, and shorten travel times.
        - **Accessibility for All:** Self-driving vehicles will cater to diverse populations, including the elderly and those with disabilities, ensuring equitable access to transportation.
        - **Sustainability:** Fully electric autonomous vehicles will contribute to a cleaner environment and lower carbon emissions.
    """)
    elif tech_focus == "Artificial Intelligence":
        st.write("**🤖 Artificial Intelligence:**")
        st.markdown("""
        AI will play a crucial role in managing city infrastructure, services, and resident needs. 
        AI-powered systems will optimize traffic flow, manage energy consumption, and even personalize resident experiences.

        - **Traffic Flow Optimization:** AI systems will analyze real-time data from vehicles, pedestrians, and citywide sensors to manage traffic lights and reduce congestion dynamically.
        - **Energy Management:** AI algorithms will monitor and control energy usage across homes, vehicles, and infrastructure, ensuring efficient consumption and minimizing waste. AI will also manage renewable energy storage and distribution.
        - **Personalized Resident Experiences:** AI will integrate with smart homes to customize lighting, temperature, and settings based on preferences, and provide tailored recommendations for transportation and entertainment.
        - **Predictive Maintenance:** AI-powered systems will monitor infrastructure like roads, utilities, and buildings, detecting issues early to minimize disruptions and ensure smooth operations.
        - **Enhanced Safety and Security:** AI will oversee security with facial recognition, anomaly detection, and surveillance, ensuring safety, and responding quickly to emergencies.
        - **Healthcare Integration:** AI will track health data from wearables, send alerts for anomalies, schedule medical consultations, and offer preventive care recommendations.
        - **Learning and Co-Evolution:** AI will continuously analyze data, adapt to evolving city needs, and improve services over time.
        - **Collaborative Robotics:** AI-driven robots will assist in tasks like delivery, caregiving, and maintenance, creating a seamless urban ecosystem.
        - **Data-Driven Decision Making:** AI will help city planners make informed decisions using large datasets from sensors, enabling long-term improvements and urban development.
    """)
    elif tech_focus == "Robotics":
        st.write("**🤖 Robotics:**")
        st.markdown("""
        Robots will assist residents with various tasks, such as:
        - **Delivering groceries and packages 📦**: Robots will autonomously deliver groceries, packages, and goods to residents' doors.
        - **Providing companionship and assistance to the elderly 👵**: Social robots will offer companionship, mobility support, and medication reminders for the elderly.
        - **Maintaining public spaces and infrastructure 🏗️**: Robots will handle cleaning, landscaping, waste collection, and infrastructure repairs, ensuring well-maintained public areas.
        - **Emergency Response**: Robots will assist during emergencies, delivering supplies or helping with evacuations.
        - **Caregiving Support**: Robots will support health monitoring and mobility, helping those with limited mobility or health needs.
        - **Educational Assistance**: Robots will offer personalized learning and tutoring, enhancing educational experiences.
    """)
    elif tech_focus == "Sustainability":
        st.write("**🌱 Sustainability:**")
        st.markdown("""
        Woven City is committed to environmental sustainability. 
        Key initiatives include:
        - **Utilizing renewable energy sources like solar and wind power ☀️🌬️**: Reducing reliance on fossil fuels and lowering carbon emissions.
        - **Implementing sustainable building practices 🏡**: Using eco-friendly materials, energy-efficient designs, and solar-powered systems to minimize the environmental footprint.
        - **Reducing waste and promoting recycling ♻️**: A zero-waste approach with smart recycling systems to reduce landfill use and promote a circular economy.
        - **Water Conservation**: Recycling wastewater and rainwater for sustainable use and maintaining green spaces.
        - **Urban Farming**: Local food production through urban farms and vertical gardens to cut down transportation emissions.
        - **Electric & Autonomous Transport**: Fully electric, autonomous vehicles powered by renewable energy to reduce emissions and traffic congestion.
        - **Green Spaces**: Parks and forests dedicated to biodiversity and residents’ well-being.
    """)

# Function for "Future of Woven City" Page
def future_of_woven_city():
    st.header("🚀 The Future of Woven City")
    st.markdown("""
    - The first phase of construction is complete. ✅
    - The city is expected to welcome around **100 residents** in the initial phase. 👨‍👩‍👧‍👦
    - The total population is projected to reach approximately **2,000 residents**. 🏘️
    - Woven City is a developing project, and details may evolve over time. 🔄
    - The city will serve as a hub for testing innovations in AI, robotics, and sustainability. 🤖🌱
    - Woven City will collaborate with global experts to set a model for future smart cities. 🌍
    """)

    # Interactive Slider for Population Projection
    st.subheader("📊 Population Projection")
    population = st.slider("Select the projected population of Woven City:", 0, 2000, 100)
    st.write(f"Woven City is projected to have **{population} residents** in the future.")

    # Progress Bar for Fun
    st.subheader("🏗️ Construction Progress")
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

# Function for "Conclusion" Page
def conclusion():
    st.header("🎯 Conclusion")
    st.markdown("""
    Woven City is a **bold and innovative project** that could revolutionize the way we live in cities. 
    It is a living laboratory for the future of urban living, paving the way for smarter, safer, and more efficient cities.

    *"The best way to predict the future is to create it."* – **Abraham Lincoln**

    Woven City is creating the future of urban living, where cutting-edge technology meets sustainability and visionary design.
    """)

# Top Navigation Menu
menu = ["Home", "What is Woven City?", "Key Features", "Technology Focus", "Future of Woven City", "Conclusion"]
cols = st.columns(len(menu))

for i, page_name in enumerate(menu):
    if cols[i].button(page_name):
        update_page(page_name)

# Display the selected page based on session state
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "What is Woven City?":
    what_is_woven_city()
elif st.session_state.page == "Key Features":
    key_features()
elif st.session_state.page == "Technology Focus":
    technology_focus()
elif st.session_state.page == "Future of Woven City":
    future_of_woven_city()
elif st.session_state.page == "Conclusion":
    conclusion()

# Footer
st.markdown("---")
st.markdown("© By Ankit Anand")
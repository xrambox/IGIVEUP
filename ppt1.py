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
    st.write("Welcome to the Woven City Explorer! Use the menu above to navigate through different sections.")
    st.markdown("""
    - **What is Woven City?** – Learn about the concept and purpose of Woven City.
    - **Key Features** – Explore the unique features of this futuristic city.
    - **Technology Focus** – Dive into the technologies driving Woven City.
    - **Future of Woven City** – Discover the future plans and projections.
    - **Conclusion** – Wrap up with the significance of this project.
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
        """)
    elif tech_focus == "Artificial Intelligence":
        st.write("**🤖 Artificial Intelligence:**")
        st.markdown("""
            AI will play a crucial role in managing city infrastructure, services, and resident needs. 
            AI-powered systems will optimize traffic flow, manage energy consumption, and even personalize resident experiences.
        """)
    elif tech_focus == "Robotics":
        st.write("**🤖 Robotics:**")
        st.markdown("""
            Robots will assist residents with various tasks, such as:
            - Delivering groceries and packages 📦
            - Providing companionship and assistance to the elderly 👵
            - Maintaining public spaces and infrastructure 🏗️
        """)
    elif tech_focus == "Sustainability":
        st.write("**🌱 Sustainability:**")
        st.markdown("""
            Woven City is committed to environmental sustainability. 
            Key initiatives include:
            - Utilizing renewable energy sources like solar and wind power ☀️🌬️
            - Implementing sustainable building practices 🏡
            - Reducing waste and promoting recycling ♻️
        """)

# Function for "Future of Woven City" Page
def future_of_woven_city():
    st.header("🚀 The Future of Woven City")
    st.markdown("""
    - The first phase of construction is complete. ✅
    - The city is expected to welcome around **100 residents** in the initial phase. 👨‍👩‍👧‍👦
    - The total population is projected to reach approximately **2,000 residents**. 🏘️
    - Woven City is a developing project, and details may evolve over time. 🔄
    """)

    # Interactive Slider for Population Projection
    st.subheader("📊 Population Projection")
    population = st.slider("Select the projected population of Woven City:", 100, 5000, 2000)
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
    It is a living laboratory for the future of urban living, and it is sure to be a fascinating place to watch as it develops.
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
# Simple Chatbot for Financial Queries

# Define the financial data for the companies
financial_data = {
    "Microsoft": {
        "total_revenue": "198.27 billion",
        "net_income": "72.74 billion",
        "net_income_change": "Increased by 5.4% from last year",
        "total_assets": "365.45 billion",
        "cash_flow_operating": "76.21 billion"
    },
    "Tesla": {
        "total_revenue": "53.85 billion",
        "net_income": "12.55 billion",
        "net_income_change": "Increased by 22% from last year",
        "total_assets": "87.83 billion",
        "cash_flow_operating": "5.86 billion"
    },
    "Apple": {
        "total_revenue": "394.33 billion",
        "net_income": "99.80 billion",
        "net_income_change": "Increased by 7.3% from last year",
        "total_assets": "383.60 billion",
        "cash_flow_operating": "106.34 billion"
    }
}

# Function to respond to user queries
def simple_chatbot(user_query):
    company = "Microsoft"  # Can be dynamically changed, assuming the user is asking for a specific company
    # Example for Microsoft, similar logic can be implemented for Tesla, Apple, or dynamic input from users
    
    if user_query == "What is the total revenue?":
        return f"The total revenue for {company} is {financial_data[company]['total_revenue']}."
    elif user_query == "How has net income changed over the last year?":
        return f"The net income for {company} has {financial_data[company]['net_income_change']}."
    elif user_query == "What is the total net income?":
        return f"The total net income for {company} is {financial_data[company]['net_income']}."
    elif user_query == "What are the total assets?":
        return f"The total assets for {company} are {financial_data[company]['total_assets']}."
    elif user_query == "What is the cash flow from operating activities?":
        return f"The cash flow from operating activities for {company} is {financial_data[company]['cash_flow_operating']}."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Sample interaction
user_query = input("Enter your financial query: ")
print(simple_chatbot(user_query))

# Importing modules
import re
import pandas as pd

# To convert text into data frame in desired form
def preprocess(data):
    
    # Regular expression
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    
    # Split text file into messages & dates based on pattern
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    
    # Creating data frame
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    
    # convert dates type
    try:
        df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ')
    except:
        df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:# For each message in user_message
        
        # Split message based on '([\w\W]+?):\s'
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]: 
            # User name
            users.append(entry[1])
            # Only message
            messages.append(" ".join(entry[2:]))
        else:
            # Adding group notifications
            users.append('group_notification')
            
            # Null value
            messages.append(entry[0])
    
    # Creating new columns
    df['user'] = users
    df['message'] = messages
    
    # Remove columns of no use
    df.drop(columns=['user_message'], inplace=True)
    
    # Extract date
    df['only_date'] = df['date'].dt.date
    
    # Extract year
    df['year'] = df['date'].dt.year
    
    # Extract month
    df['month_num'] = df['date'].dt.month
    
    # Extract month name
    df['month'] = df['date'].dt.month_name()
    
    # Extract day
    df['day'] = df['date'].dt.day
    
    # Extract day name
    df['day_name'] = df['date'].dt.day_name()
    
    # Extract hour
    df['hour'] = df['date'].dt.hour
    
    # Extract minute
    df['minute'] = df['date'].dt.minute

    # Remove entries having user as group_notification
    df = df[df['user'] != 'group_notification']
    
    # Returning preprocessed data frame
    return df

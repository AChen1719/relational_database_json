import json


def write_csv_file(event_sign_up):
    file2 = open('event_sign_up.csv', 'w')
    file2.write('firstname, lastname, email, role, event\n')
    for events in event_sign_up:
        file2.write(
            str(events[0]) + ',' + str(events[1]) + ',' + str(events[2]) + ',' + str(events[3]) + ',' + str(events[4]) + ',' + str(events[5]) + '\n')
    file2.close()


def ask_user_choose_events(events_list):
    # create an empty events_list
    user_eventslist = []
    print('Here are the list of events you can choose from: ')
    while True:
        num = 1
        for all_events in events_list:
            print(num, '-', all_events.get('email'), 'by', all_events.get('event'))
            num += 1
        user_choice = int(input('Enter the number of event you like: ')) - 1
        chosen_events_dictionary = events_list[user_choice]
        print('Great! You signed up', chosen_events_dictionary.get('event'), 'by', chosen_events_dictionary.get('email'))
        put_event_in_playlist = list()
        put_event_in_playlist.append(chosen_events_dictionary.get('firstname'))
        put_event_in_playlist.append(chosen_events_dictionary.get('lastname'))
        put_event_in_playlist.append(chosen_events_dictionary.get('email'))
        put_event_in_playlist.append(chosen_events_dictionary.get('job role'))
        put_event_in_playlist.append(chosen_events_dictionary.get('event'))
        chose_again = input('Do you want to sign up another event Y/ N: ').upper()
        if chose_again == 'N':
            print('I like your new events list !')
            break
    # return the playlist which was created earlier
    return user_eventslist


def read_json_file():
    # open the json file with 'r' mode
    file1 = open("event_sign_up.csv", 'r')
    # copy the contents of the file to the memory
    chosen_events_dictionary = json.load(file1)
    # reach into the contents and get the list of events
    events_list = chosen_events_dictionary.get("events_list")
    # close the file
    file1.close()
    # return the list of events
    return events_list


def main():
    events_list = read_json_file()
    user_eventslist = ask_user_choose_events(events_list)
    write_csv_file(user_eventslist)


main()

import yaml
class MessageID:
    file = '/Users/ngoc_toan/PycharmProjects/MyApplication/web2py/applications/FristSample/views/message_error.yml'
    def yaml_load(filepath):
        with open(filepath, "r") as file_descriptor:
            data = yaml.load(file_descriptor)
            return data

    data = yaml_load(file)
    list_message_id = data.get('errors')

    message_error_key = list_message_id['messsage.ID001.Key']
    message_error_empty = list_message_id['messsage.ID002.Empty']
    message_error_format_date = list_message_id['messsage.ID003.Date']
    message_error_age = list_message_id['messsage.ID004.Age']
    message_error_email = list_message_id['messsage.ID005.Email']
    message_error_leght = list_message_id['messsage.ID006.Lenght']
    message_error_range_age = list_message_id['messsage.ID007.Range']
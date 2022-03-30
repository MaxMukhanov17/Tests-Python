documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}


def get_name(doc):
  input_p = input('Введите номер документа: ')
  is_found = False
  for people in doc:
    if input_p == people['number']:
      return people['name']
  if is_found == False:
    return 'Такой номер документа не найден. Введите снова!'
  else:
    return None

def get_shelf(direct):
  input_p = input('Введите номер документа: ')
  for key,values in direct.items():
    if input_p in values:
      return key 
  return 'Такого номера не существует. Введите снова!'

def get_list(doc):
  list_doc = []
  for lists in doc:
    list_doc.append(list(lists.values()))
  return list_doc

def add_doc(docs,direct):
  input_num = input("Введите номер документа: ")
  input_type = input("Введите тип документа: ")
  input_name = input("Введите имя владельца: ")
  input_shelf = input("Введите номер полки на котором будет храниться документ: ")
  doc = {"type": input_type, "number": input_num, "name": input_name}
  docs.append(doc)
  for keys in direct:
    if input_shelf in direct.keys():
      direct[input_shelf].append(doc['number'])
      return 'Документ добавлен.'
  return 'Такой полки не существует. Введите снова'

def main(doc,direct):
  while True:
    user_input = input("Введите команду: ")
    if user_input == 'p':
      print(f'Имя владельца, которому пренадлежит документ: {get_name(documents)}')
    elif user_input == 's':
      print(f'Номер полки на которой хранится документ: {get_shelf(directories)}')
    elif user_input == 'l':
      print(f'Список всех документов: {get_list(documents)}')
    elif user_input == 'a':
      print(f'Добавление документа в каталог и перечень полок: {add_doc(documents,directories)}')
    else:
      print('До свидания!')
      break


if __name__ == '__main__': 
    # main(documents,directories)
    print(get_shelf(directories))
# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

#
l = my_dict.items()
print l

# def function_dic(my_dict):
#     # for x in range(0, len(my_dict)):
#     #     print x
#     for key, data in my_dict.iteritems():
#         return key, " = ", data

# function_dic(my_dict)
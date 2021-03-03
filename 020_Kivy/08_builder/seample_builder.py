from kivy.lang import Builder

Builder.load_file('mkivy.kv')

# Builder.load_string(
# '''
# <MyLayout>
#     Label:
#         text: 'Hello World'
#         font_size: 72
#     # FloatLayout:
#     #     size: root.width, root.height
    
#     #     Button:
#     #             text: 'Hello World!!'
#     #             size_hint: .5, .5
#     #             # pos_hint: {'center_x':.5, 'center_y': .5}
#     #             pos: 100, 100
#     #     Button:
#     #         pos_hint: {"x": 0.1, "top": 0.9}
#     #         text: "Insert story about company here"
#     #         size_hint: 0.8, 0.4
# ''')
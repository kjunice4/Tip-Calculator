#Tip Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "Tip Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"         
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "KSquared-math,LLC ©"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 

""")

#Menu Page
Builder.load_string("""
<Menu>:
    id: Menu
    name: "Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
            
            Button:
                font_size: 75
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height:400
                text: "Tip Calculator"
                on_release:
                    app.root.current = "Tip_Calculator"
                    root.manager.transition.direction = "left" 
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Visit KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
            
""")

#Tip calc
Builder.load_string("""
<Tip_Calculator>
    id:Tip_Calculator
    name:"Tip_Calculator"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Tip Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        Bill.text = ""
                        Percent.text = ""
                        Split.text = ""
                        list_of_steps.clear_widgets()       
                                   
            TextInput:
                id: Bill
                text: Bill.text
                hint_text: "Bill: $"
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10
                input_filter: lambda text, from_undo: text[:6 - len(Bill.text)]           
        
            TextInput:
                id: Percent
                text: Percent.text
                hint_text: "Percent: %"
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10              
                input_filter: lambda text, from_undo: text[:2 - len(Percent.text)]         
                
            TextInput:
                id: Split
                text: Split.text
                hint_text: "Split:"
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10              
                input_filter: lambda text, from_undo: text[:3 - len(Split.text)] 
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Tip_Calculator.steps(Bill.text + "$" + Percent.text + "&" + Split.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Tip_Calculator(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Tip_Calculator, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = "Menu"
    layouts = []
    def steps(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            # Tip Calculator
            print("~~~~~~~~~~~~~~~~")
            print(entry)
            bill = entry[:entry.find("$")]
            print()
            print("Bill",bill)
            perc = entry[entry.find("$")+1:entry.find("&")]
            
            if perc == "":
                perc = 0
                print("perc",perc)
            
            tip = str(float(bill) * float(perc) / 100)
            print()
            print("Tip: $",tip)
            
            total = str(float(bill) + (float(bill) * float(perc) / 100))
            print()
            print("Total Bill: $", total)
            
            split = entry[entry.find("&")+1:]
            print()
            print("split",split)
            
            if split == "":
                split = 0
                print()
                print("Split:",split)
            
            if int(split) > 1:
                bill_split = str(float(bill) / float(split))
                print("Bill split", bill_split)
                
                tip_split = str(float(tip) / float(split))
                print("tip_split",tip_split)
                
                total_split = str(float(total) / float(split))
                print("total_split",total_split)
                
                self.ids.list_of_steps.add_widget(Label(text= "Bill = $" + "{:,.2f}".format(float(bill)) ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                 
                self.ids.list_of_steps.add_widget(Label(text= "Percent for Tip = " + str(perc) + "%" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                 
                self.ids.list_of_steps.add_widget(Label(text= "Tip = $" + "{:,.2f}".format(float(tip)),font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                self.ids.list_of_steps.add_widget(Label(text= "Total Bill = $" + "{:,.2f}".format(float(total)),font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout) 

            
            if float(split) == 1 or float(split) == 0: 
                self.ids.list_of_steps.add_widget(Label(text= "Bill = $" + "{:,.2f}".format(float(bill)) ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                 
                self.ids.list_of_steps.add_widget(Label(text= "Percent for Tip = " + str(perc) + "%" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                self.ids.list_of_steps.add_widget(Label(text= "Tip = $" + "{:,.2f}".format(float(tip)),font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                self.ids.list_of_steps.add_widget(Label(text= "Total Bill = ${:,.2f}".format(float(total)) ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            elif float(split) > 1:
                self.ids.list_of_steps.add_widget(Label(text= "${:,.2f}".format(float(bill)) + " bill split " + str(split) + " ways = ${:,.2f}".format(float(bill_split)) ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                self.ids.list_of_steps.add_widget(Label(text= "${:,.2f}".format(float(tip)) + " tip split " + str(split) + " ways = ${:,.2f}".format(float(tip_split)) ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                self.ids.list_of_steps.add_widget(Label(text= "Each person's total = ${:,.2f}".format(float(total_split)) ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
                print("Invalid Input")
                self.ids.list_of_steps.add_widget(Label(text= "" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            
        except Exception:
            try:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                    
            except Exception:               
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)  
                
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(Tip_Calculator(name="Tip_Calculator"))     
sm.current = "Homepage"


class Tip_Calculator(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Tip_Calculator().run()
    

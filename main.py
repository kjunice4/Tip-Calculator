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
                app.root.current = "Tip_Calculator"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Exponents Solver"
            on_release:
                app.root.current = "Tip_Calculator"
                root.manager.transition.direction = "left" 

""")

#EXPONENTS STEPS
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
                    text: "Clear Entry"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        Bill.text = ""
                        Percent.text = ""
                        Split.text = ""
                        
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
                                   
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                Label:
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    text: "Bill: $"
                                                        
                TextInput:
                    id: Bill
                    text: Bill.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:6 - len(Bill.text)]           
            
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5        
        
                Label:
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    text: "Percent: %"
                                                    
                TextInput:
                    id: Percent
                    text: Percent.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10              
                    input_filter: lambda text, from_undo: text[:2 - len(Percent.text)]         
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5        
        
                Label:
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    text: "Split:"
                                                    
                TextInput:
                    id: Split
                    text: Split.text
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
            sm.current = sm.previous()    
    layouts = []
    def steps(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            # Tip Calculator
            print(entry)
            bill = entry[:entry.find("$")]
            print("Bill",bill)
            perc = entry[entry.find("$")+1:entry.find("&")]
            
            tip = str(float(bill) * float(perc) / 100)
            
            print()
            print("Tip: $",tip)
            
            total = str(float(bill) + (float(bill) * float(perc) / 100))
            print()
            print("Total Bill: $", total)
            
            split = entry[entry.find("&")+1:]
            print("split",split)
            
            if split == "":
                split = 0
            
            self.ids.list_of_steps.add_widget(Label(text= "Bill = $" + "{:,.2f}".format(float(bill)) ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            self.ids.list_of_steps.add_widget(Label(text= "Percent for Tip = " + perc + "%" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            self.ids.list_of_steps.add_widget(Label(text= "Tip = $" + "{:,.2f}".format(float(tip)),font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            self.ids.list_of_steps.add_widget(Label(text= "Total Bill = $" + "{:,.2f}".format(float(total)) ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            if float(split) == 1 or float(split) == 0: 
                None
            elif float(split) > 1:
                print()
                print("Bill after split: $",float(total)/float(split),"each")
                
                split_up = str(float(total)/float(split))
                split_up = "{:,.2f}".format(float(split_up))
                print("Split_up",split_up)
                
                self.ids.list_of_steps.add_widget(Label(text= "Split " + split + " ways = $" + split_up + " each",font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
            else:
                print("Invalid Entry")
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
        except Exception:
            try:
                self.ids.list_of_steps.add_widget(Label(text= "Out Of Range" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                    
            except Exception:               
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)  
                
class Homepage(Screen):
    pass            

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Tip_Calculator(name="Tip_Calculator"))     
sm.current = "Homepage"


class Tip_Calculator(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Tip_Calculator().run()
    


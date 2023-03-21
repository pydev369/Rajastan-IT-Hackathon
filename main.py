


import flet as ft
from flet import Container
import datetime
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# from alert import bs,dlg,dlg_modal,show_bs,open_dlg,open_dlg_modal
from flet import NavigationDestination, NavigationBar, icons
# from markdwn_temp import  row_continer




def main(page: ft.Page):

    
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
    page.theme_mode = "dark"
        
    def theme_select(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        switch_theme.label = "Light" if page.theme_mode == "light" else "Dark"
        page.update()


    switch_theme = ft.Switch(label="Light", on_change=theme_select)
      
        # todo ####### ALERTS #########  
    stock_qty = 11
    cash = 29000
    
    scan_alert = f'alert'
    
    ##
# todo ####### ALERTS #########  
    stock_qty = 11
    cash = '*****'
    order_msg = f"Wellcome to The  World of Smart city. "
    scan_alert = f'alert'   
    demo_var = 369
    order_update_alert = " "
    
    ##* Order Notification ########
    def show_snackbar(e):
        page.snack_bar = ft.SnackBar(ft.Text(order_msg),
        action_color= "blue",
        bgcolor=ft.colors.GREEN_600,
        on_action= ft.Text("Holdings"),        
        )
        page.snack_bar.open = True
        page.update()
        
    def savelater_snackbar(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Current Traffic Status : Congested @{datetime.datetime.now().strftime('%d-%b-%Y %a %H:%M:%S')}"),
        action_color= "blue",
        bgcolor=ft.colors.RED_600,
        on_action= ft.Text(""),        
        )
        page.snack_bar.open = True
        page.update()        
    ##*   Banner      #######
    
    symbol = "AI Smart City"
    def close_banner(e):
        # savelater_snackbar
        page.banner.open = False        
        page.update()

    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(f"Placed NFT Order on {datetime.datetime.now().strftime('%d-%b-%Y %a %H:%M:%S')}\n Want to Receive Future  Updates",color='black',weight='bold'),         
        
        actions=[
            ft.TextButton("BUY", on_click=show_snackbar),            
            ft.TextButton("Save for Later", on_click=savelater_snackbar),
            ft.TextButton("Ignore", on_click=close_banner),
            ft.TextButton("", ),
        ],
    )

    def show_banner_click(e):
        page.banner.open = True
        page.update()

    banner_alert = ft.ElevatedButton("Trade", on_click=show_banner_click)
        
    # page.overlay.append(bs)    
    def show_snackbar(e):
        page.snack_bar = ft.SnackBar(ft.Text(f'{order_msg}'),
        action_color= "blue",
        bgcolor="green",
        on_action= ft.Text("Check Holdings")
        )
        page.snack_bar.open = True
        page.update()
        
    
          
    notify_1 = '9'
    pnl =  '30'
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MENU_OUTLINED),
        leading_width=40,
        title=ft.Text("AI Smart City"), ##Resilience  Adaptive Serene#
        
        center_title=False,
        bgcolor=ft.colors.BLACK26 ,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,on_click=show_snackbar),
            ft.Text(""),
            
            # ft.FilledButton(f"Total Market Share {pnl} %",icon=ft.icons.CURRENCY_RUPEE,height=30,icon_color="green"),
            ft.TextField(hint_text="Smart City Services", height =300,width=300),
            ft.IconButton(ft.icons.SEARCH_ROUNDED) ,
            ft.IconButton(ft.icons.BALLOT,content=(ft.Text(f'{notify_1}')),icon_color = ft.colors.BLUE_ACCENT_200),
            ft.IconButton(ft.icons.FILTER_3_ROUNDED,icon_color = ft.colors.GREEN_ACCENT_100),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Alerts"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(text="Checked Trigger", checked=False, on_click=check_item_clicked),
                      
                ]
            ),
            switch_theme,
        ],
    )
    
    
    row_continer= ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(""),
                            margin=10,
                            padding=10,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.BLUE_ACCENT_100,
                            width=850,
                            height=950,
                            border_radius=20,
                        ),
                    ],
                    alignment="center",
                )

    ##* ------- #########
    ######!########

    
    img = ft.Image(
        src=r".\ppt_photos\Moto2023-03-20 221702.png",
        #f"https://github.com/pydev369/ClioDerma-Flow-Hackathon2023FEB21-28/blob/Images/image0.jpeg",
        width=200,
        height=150,
        fit=ft.ImageFit.CONTAIN,
    )    

    def show_design(e):
        # page.views.clear()
        page.append(img)
        page.update()



    ##* ------- #########
    ######!########
    ##* Card With List-Tile #########

    card_basic1 =    ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [                          
                           
                        ft.Divider(thickness=2,color=ft.colors.CYAN_400),
                        ft.ListTile(
                            leading=ft.IconButton(ft.icons.AREA_CHART_OUTLINED,icon_color='blue'),
                            
                            title=ft.Text("Water Efficiency",color='blue'),
                                subtitle=ft.Text("Green City would result in potable water savings to the tune of 30-40% by adopting practices such as "),
                                
                            # trailing=ft.PopupMenuButton(
                            #     icon=ft.icons.MORE_VERT,
                                # items=[
                                #     ft.PopupMenuItem(text=""),
                                #     # ft.PopupMenuItem(text=""),
                                # ],
                            # ),
                        ),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text('Usgage of Surface water & minimalistic Usage of Ground Water',size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Treatment & reuse of waste water.",size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800), 
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Rain waterwater Harvesting etc.",size=12)),
                        
                        # ft.Row(
                        #     [ft.TextButton("",disabled =True),ft.OutlinedButton("Buy",icon=ft.icons.EDIT_ATTRIBUTES,icon_color='blue',on_click=show_banner_click),
                        #         # ft.OutlinedButton("",icon=ft.icons.ADD_BOX,icon_color='green'), ft.OutlinedButton("Add Cart")
                        #         ],
                        #     alignment="end",
                        # )
                                                                         
                    ]
                ),
                width=350,height=450,
                padding=2,
            )
        )    
        ######################  
        
        
    card_basic2 =    ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [                          
                           
                        ft.Divider(thickness=2,color=ft.colors.CYAN_400),      
                                ft.ListTile(
                            leading=ft.IconButton(ft.icons.LIGHTBULB_OUTLINE_ROUNDED,icon_color='yellow'),
                            
                            title=ft.Text("Energy Efficiency",color='Blue'),
                                subtitle=ft.Text("Power generation using various renewable energy technologies and Green concepts can significantly reduce the power supply demand of the city leading to energy savings to the tune of 20-30%."),
                            ),
                            ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text('Efficient Cooling Systems',size=12)),
                            ft.Divider(thickness=1,color=ft.colors.YELLOW_800),   
                            ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Energy Efficient Devices to create less carbon foorprint",size=12))
                      
                        # ), 
                    ]
                ),
                width=350,height=450,
                padding=2,
            )
        )                            

### * ###################
    
     
     
     
     
    #########
       
    card_develop =    ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [                          
                           
                        ft.Divider(thickness=2,color=ft.colors.CYAN_400),
                        ft.ListTile(
                            leading=ft.IconButton(ft.icons.AREA_CHART_OUTLINED,icon_color='blue'),
                            
                            title=ft.Text("Green Cities promote effective land use by encouraging land use mix and higher densities to ensure compact development. These planning concepts are gaining prime importance offering multiple benefits as mentioned below:",color='blue'),
                                subtitle=ft.Text(""),
                                
                         
                        ),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text('Higher density and compact development.',size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Promote transit oriented development.",size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Preservation and Restoration of Water Bodies & Eco-sensitive zones.",size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Reduces distances between home and workplaces.",size=12)),
                                            
                                                                         
                    ]
                ),
                width=550,height=550,
                padding=2,
            )
        ) 
    # todo  container
    
    images = ft.Row(expand=1, wrap=False, scroll="always")
    container_col = ft.Container(
                                content=ft.Row([card_basic1,card_basic2],alignment='spaceAround'),
                                border_radius=8,
                                padding=5,
                                width=800,
                                height=400,
                                gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_center,
                                    end=ft.alignment.bottom_center,
                                   colors=[ft.colors.BLUE, ft.colors.YELLOW],
                                ),                              
                                         
                                # bgcolor=ft.colors.BLACK
                                )
                                
    
   # todo
    # card_container =
    
    
    
    ## todo TAB_with_card

    row_card = ft.Row(scroll=True)  
    tab_bar_content = []
    row_card.controls.append(
        ft.Card(
                elevation=30,
                content=ft.Container(
                width=160,
                height=160,
                padding=15,
                border_radius= 10,#ft.border_radius.symmetric(vertical=border.BorderSide(5,"Orange")),
                bgcolor='white',
                    content=ft.Text("Coming Soon",color="green")
                )       
        
        )    
    )    
    #########
       
    card_mobility =    ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [                          
                           
                        ft.Divider(thickness=2,color=ft.colors.CYAN_400),
                        ft.ListTile(
                            leading=ft.IconButton(ft.icons.AREA_CHART_OUTLINED,icon_color='blue'),
                            
                            title=ft.Text("",color='blue'),
                                subtitle=ft.Text("Green City increases opportunities for bicycling, pedestrian friendly network, reduction in the number of automobile trips, promoting public transportation and use of vehicles with alternative fuels. "),
                                
                            # trailing=ft.PopupMenuButton(
                            #     icon=ft.icons.MORE_VERT,
                                # items=[
                                #     ft.PopupMenuItem(text=""),
                                #     # ft.PopupMenuItem(text=""),
                                # ],
                            # ),
                        ),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text('In a nutshell, efficient transportation planning enable cities to accommodate all modes of travel, including walking, bicycling and public transportation which are vital parts of reducing the carbon footprint in cities.',size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("AI controlled traffic to avoid traffic congestion with smart peak hour traffc routing.",size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Usage of Drones for dynamic traffic status updates.",size=12)),
                     
                                                                         
                    ]
                ),
                width=350,height=550,
                padding=2,
            )
        )    
        ######################  
      
    card_wastemanage =    ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [                          
                           
                        ft.Divider(thickness=2,color=ft.colors.CYAN_400),
                        ft.ListTile(
                            leading=ft.IconButton(ft.icons.AREA_CHART_OUTLINED,icon_color='blue'),
                            
                            title=ft.Text("",color='blue'),
                                subtitle=ft.Text("Waste management in Green Cities takes into account planning and implementation of efficient systems for collection, transportation, treatment, recycling and reuse or disposal of municipal solid waste."),
                                
                      
                        ),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text('Create compost from solid waste helps green Cities to achieve zero waste discharge to landfill sites.',size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Proper segregation of waste on source by encouraging citizen to follow rules by reward points.",size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Usage of Drones for routine tracking of implementation of solid waste mangement policies.",size=12)),
                     
                                                                         
                    ]
                ),
                width=350,height=550,
                padding=2,
            )
        )    
    
    ###########
    card_wastemanage =     ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [                          
                           
                        ft.Divider(thickness=2,color=ft.colors.CYAN_400),
                        ft.ListTile(
                            leading=ft.IconButton(ft.icons.AREA_CHART_OUTLINED,icon_color='blue'),
                            
                            title=ft.Text("",color='blue'),
                                subtitle=ft.Text("Green City increases opportunities for bicycling, pedestrian friendly network, reduction in the number of automobile trips, promoting public transportation and use of vehicles with alternative fuels. "),
                                
                            # trailing=ft.PopupMenuButton(
                            #     icon=ft.icons.MORE_VERT,
                                # items=[
                                #     ft.PopupMenuItem(text=""),
                                #     # ft.PopupMenuItem(text=""),
                                # ],
                            # ),
                        ),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text('In a nutshell, efficient transportation planning enable cities to accommodate all modes of travel, including walking, bicycling and public transportation which are vital parts of reducing the carbon footprint in cities.',size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("AI controlled traffic to avoid traffic congestion with smart peak hour traffc routing.",size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Usage of Drones for dynamic traffic status updates.",size=12)),
                     
                                                                         
                    ]
                ),
                width=350,height=550,
                padding=2,
            )
        )    
        ######################  
      
    card_livable =    ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [                          
                           
                        ft.Divider(thickness=2,color=ft.colors.CYAN_400),
                        ft.ListTile(
                            leading=ft.IconButton(ft.icons.AREA_CHART_OUTLINED,icon_color='blue'),
                            
                            title=ft.Text("",color='blue'),
                                subtitle=ft.Text("Reduced commuting time, accessible recreational spaces."),
                                
                      
                        ),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text('Increase in green cover, continuous environmental monitoring shall enhance the quality of life thereby making the city healthier and liveable.',size=12)),
                        ft.Divider(thickness=1,color=ft.colors.YELLOW_800),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text("Sustainable environment friendly policies control pollution ,imporves vitality of citizens.",size=12)),
                        
                                                                         
                    ]
                ),
                width=350,height=450,
                padding=2,
            )
        )    
    

        ######################  
      
    card_egov =    ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [                          
                           
                        ft.Divider(thickness=2,color=ft.colors.CYAN_400),
                        ft.ListTile(
                            leading=ft.IconButton(ft.icons.AREA_CHART_OUTLINED,icon_color='blue'),
                            
                            title=ft.Text("",color='blue'),
                                subtitle=ft.Text("Greater no. govt policies will be offered online(e-gov portal or mobile app).Hence govt. services will be more affordable & more transparet"),
                                
                      
                        ),   
                        ft.ListTile(leading=ft.IconButton(ft.icons.ARROW_CIRCLE_RIGHT,icon_color='blue'),title=ft.Text('Increase in green cover, continuous environmental monitoring shall enhance the quality of life thereby making the city healthier and liveable.',size=12)),

                                                                         
                    ]
                ),
                width=350,height=450,
                padding=2,
            )
        )    
    
    
    
    
    
    ################
    tab_item = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs= [
        
            ft.Tab(
                text="Efficient Land Use",
                content=ft.Container(
                    content=card_develop, alignment= ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Sustainabilty",
                content=ft.Container(
                    content=container_col, alignment= ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Smart Mobilty",                
                content=ft.Container(
                    content=card_mobility, alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="E-Governance",
                content=ft.Container(
                    content=card_egov, alignment= ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Solid Waste Management",
                content=ft.Container(
                    content=card_wastemanage, alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                text="Livable",
                content=ft.Container(
                    content=card_livable, alignment=ft.alignment.center
                ),
            ),
            # ft.Tab(
            #     text="Global Presence",
            #     # tab_content=ft.Icon(name = ft.icons.ARROW_FORWARD_IOS),
            #     content=ft.Container(
            #         # content=ft.Text('Coming Soon'), alignment=ft.alignment.center
            #     ),
            # ),
        ],
        col=6,width=800,expand=3,
    )
    
    # page.navigation_bar = NavigationBar(
    #     destinations=[
    #         NavigationDestination(icon=icons.HOME, label="HOME"),
    #         NavigationDestination(icon=icons.MONETIZATION_ON, label="Supports"),
    #         NavigationDestination(icon=icons.HAIL_SHARP, label=""),
    #         NavigationDestination(icon=icons.CHARGING_STATION_ROUNDED, label="Blockchain Adoption & Vision"),
    #         NavigationDestination(
    #             icon=icons.BOOKMARK_BORDER,
    #             selected_icon=icons.BOOKMARK,
    #             label="Behind The Scene Team",
    #         ),
    #     ]
    # )
    


## ? Navigate  Routing
    navigation_rail = ft.NavigationRail(
        selected_index=0,
        label_type="all",
        extended=True,
        height=600,
        min_width=50,
        min_extended_width=100,
        leading=ft.FloatingActionButton(icon=ft.icons.PRECISION_MANUFACTURING_ROUNDED , text="Design Principle",on_click=show_design),
        group_alignment=-0.9,
        disabled= False,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.BOOK, selected_icon=ft.icons.BUILD_OUTLINED, label="Compact Development",
            ),
                        

            ft.NavigationRailDestination(
                icon=ft.icons.HEALTH_AND_SAFETY,
                selected_icon_content=ft.Icon(ft.icons.HEALTH_AND_SAFETY_OUTLINED),
                label_content=ft.Text("AI & Health",color='purple'),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.VOICE_CHAT,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("Smart City Asistant",color='green',no_wrap=False),
            ),
                        
            ft.NavigationRailDestination(
                icon=ft.icons.CALENDAR_MONTH,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("Events"),
            ),
            
            
            
                     
            ft.NavigationRailDestination(
                icon=ft.icons.UPCOMING_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("Updates"),
            ),
            
                        
            ft.NavigationRailDestination(
                icon=ft.icons.TASK_ALT_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text("Feature Request"),
            ),
            
                      
            ft.NavigationRailDestination(
                icon=ft.icons.REPORT,
                selected_icon_content=ft.Icon(ft.icons.REPORT_OUTLINED ),
                label_content=ft.Text("Citzen Feedback"),
            ),
                ft.NavigationRailDestination(
                icon=ft.icons.THUMB_UP_ALT,
                selected_icon_content=ft.Icon(ft.icons.THUMB_UP_ALT),
                label_content=ft.Text("Good Citizenship Reward"),
            ),
            
            # ft.Divider(height=0.3,color= ft.colors.AMBER_100,thickness=2), # todo Divider
                                              
            ft.NavigationRailDestination(
                # icon=ft.icons.BUG_REPORT_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
                label_content=ft.Text(""),
            ),
            
            # # ft.TextField(width=200,bgcolor = 'white', border_radius =10, border_width = 1, border_color= 'white',hint_text="Enter item name"),                     
            # ft.NavigationRailDestination(
            #     icon=ft.icons.BUG_REPORT_OUTLINED,
            #     selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
            #     label_content=ft.Text(""),
            # ),
                                     
            # ft.NavigationRailDestination(
            #     icon=ft.icons.FIRE_TRUCK_SHARP,
            #     selected_icon_content=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
            #     label_content=ft.Text("Backtest"),
            # ),           
            
            # ft.Text("Broker Agonistic Customizable Trading System",no_wrap=False),
            
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )
   
    
    
    # todo########
    page.add(ft.Row())
    #     ft.Row(
    #         [
    #             rail,
    #             ft.VerticalDivider(width=1),tab_item
    #         ,],
    #         expand=True,
    #     )
    # )
    
    col = ft.Ref[ft.Column]()
    row = ft.Ref[ft.Column]()
    # ! multi_chart 

#


        
    # todo #######  checkbox & containers  ##########
    tab_col=ft.Column()
    page.add(
        ft.Row(
        [
        navigation_rail,
        ft.VerticalDivider(width=1,color= ft.colors.AMBER_300,thickness=2),
        
        tab_item,
        
        # ft.PopupMenuItem(text="Features", checked=False, on_click=check_item_clicked)]                  
            # ft.Column([ ft.Checkbox(['1m','5m','15m','1H','D','W'])], alignment="start", expand=True),
            # col = ft.Column(),
            # col.current.controls.append(t)
        ],
            expand=True,
        )
    )
    # page.title = "DRONACHARYA"
        
ft.app(name= "Clioderma",target=main,view=ft.WEB_BROWSER)

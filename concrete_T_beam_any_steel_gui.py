# -*- coding: utf-8 -*-

from __future__ import division

#Import Python Modules
import matplotlib
matplotlib.use('TKAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import Tkinter as tk
import math
import tkFont

#Import my modules
import concrete_beam_classes as concbeam

class Main_window:
    
    def __init__(self, master):
        self.master = master
        
        helv = tkFont.Font(family='Helvetica',size=8, weight='normal')
        self.menubar = tk.Menu(self.master)
        self.menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = "File", menu=self.menu)
        self.menu.add_command(label="Open")
        self.menu.add_separator()
        self.menu.add_command(label="Save Inputs")
        self.menu.add_command(label="Run")
        self.menu.add_command(label="Save Results")
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=self.quit_app)


        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(master, "config", "-menu", self.menubar)
        ## Main Frame        
        self.main_frame = tk.Frame(master, bd=2, relief='sunken', padx=5,pady=5)
        self.main_frame.pack(anchor='c', padx= 5, pady= 5, fill=tk.BOTH, expand=1)
        
        ## Entry Frame
        self.frame_entry = tk.Frame(self.main_frame, padx=2, pady=2)

        self.t_beam_flange_frame = tk.LabelFrame(self.frame_entry, text="T Beam Flange Properties", bd=1, relief='sunken', padx=2, pady=2, font=helv)

        self.section_span = tk.StringVar()
        self.section_span_label = tk.Label(self.t_beam_flange_frame, text="Beam Span (ft): ", font=helv)
        self.section_span_label.grid(row=0,column=0, pady=2)
        self.section_span_entry = tk.Entry(self.t_beam_flange_frame,textvariable=self.section_span, font=helv, width=8)
        self.section_span_entry.grid(row=0,column=1, pady=2)

        self.section_slab_thickness = tk.StringVar()
        self.section_slab_thickness_label = tk.Label(self.t_beam_flange_frame, text="Slab Thickness (in): ", font=helv)
        self.section_slab_thickness_label.grid(row=1,column=0, pady=2)
        self.section_slab_thickness_entry = tk.Entry(self.t_beam_flange_frame,textvariable=self.section_slab_thickness, font=helv, width=8)
        self.section_slab_thickness_entry.grid(row=1,column=1, pady=2)

        self.section_span_slab_left = tk.StringVar()
        self.section_span_slab_left_label = tk.Label(self.t_beam_flange_frame, text="Slab Clear Span to the Left (ft): ", font=helv)
        self.section_span_slab_left_label.grid(row=2,column=0, pady=2)
        self.section_span_slab_left_entry = tk.Entry(self.t_beam_flange_frame,textvariable=self.section_span_slab_left, font=helv, width=8)
        self.section_span_slab_left_entry.grid(row=2,column=1, pady=2)

        self.section_span_slab_right = tk.StringVar()
        self.section_span_slab_right_label = tk.Label(self.t_beam_flange_frame, text="Slab Clear Span to the Right (ft): ", font=helv)
        self.section_span_slab_right_label.grid(row=3,column=0, pady=2)
        self.section_span_slab_right_entry = tk.Entry(self.t_beam_flange_frame,textvariable=self.section_span_slab_right, font=helv, width=8)
        self.section_span_slab_right_entry.grid(row=3,column=1, pady=2)

        self.section_or_label = tk.Label(self.t_beam_flange_frame, text="Or", font=helv)
        self.section_or_label.grid(row=0,column=2, pady=2)

        self.section_bf = tk.StringVar()
        self.section_bf_label = tk.Label(self.t_beam_flange_frame, text="Flange Width (in): ", font=helv)
        self.section_bf_label.grid(row=0,column=3, pady=2)
        self.section_bf_entry = tk.Entry(self.t_beam_flange_frame,textvariable=self.section_bf, font=helv, width=8)
        self.section_bf_entry.grid(row=0,column=4, pady=2)

        self.section_hf = tk.StringVar()
        self.section_hf_label = tk.Label(self.t_beam_flange_frame, text="Flange Thickness (in): ", font=helv)
        self.section_hf_label.grid(row=1,column=3, pady=2)
        self.section_hf_entry = tk.Entry(self.t_beam_flange_frame,textvariable=self.section_hf, font=helv, width=8)
        self.section_hf_entry.grid(row=1,column=4, pady=2)

        self.t_beam_flange_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.beam_props_frame = tk.LabelFrame(self.frame_entry, text="Beam Properties - Note H is total height inlcusive of slab/flange thickness", bd=1, relief='sunken', padx=2, pady=2, font=helv)

        self.section_info = tk.StringVar()
        self.section_info_label = tk.Label(self.beam_props_frame, text="Section Label : ", font=helv)
        self.section_info_label.grid(row=0,column=0, pady=2)
        self.section_info_entry = tk.Entry(self.beam_props_frame,textvariable=self.section_info, font=helv, width=8)
        self.section_info_entry.grid(row=0,column=1, pady=2)

        self.section_b = tk.StringVar()
        self.section_b_label = tk.Label(self.beam_props_frame, text="B (in) : ", font=helv)
        self.section_b_label.grid(row=1,column=0, pady=2)
        self.section_b_entry = tk.Entry(self.beam_props_frame,textvariable=self.section_b, font=helv, width=8)
        self.section_b_entry.grid(row=1,column=1, pady=2)

        self.section_h = tk.StringVar()
        self.section_h_label = tk.Label(self.beam_props_frame, text="H (in) : ", font=helv)
        self.section_h_label.grid(row=2,column=0, pady=2)
        self.section_h_entry = tk.Entry(self.beam_props_frame,textvariable=self.section_h, font=helv, width=8)
        self.section_h_entry.grid(row=2,column=1, pady=2)

        self.section_cover = tk.StringVar()
        self.section_cover_label = tk.Label(self.beam_props_frame, text="Cover (in) : ", font=helv)
        self.section_cover_label.grid(row=3,column=0, pady=2)
        self.section_cover_entry = tk.Entry(self.beam_props_frame,textvariable=self.section_cover, font=helv, width=8)
        self.section_cover_entry.grid(row=3,column=1, pady=2)

        self.section_agg = tk.StringVar()
        self.section_agg.set('0.75')
        self.section_agg_label = tk.Label(self.beam_props_frame, text="Aggregate Size (in) : ", font=helv)
        self.section_agg_label.grid(row=4,column=0, pady=2)
        self.section_agg_menu = tk.OptionMenu(self.beam_props_frame, self.section_agg, '0.75', '1')
        self.section_agg_menu.config(font=helv)
        self.section_agg_menu.grid(row=4, column=1, padx= 2, sticky=tk.W)

        self.section_fprimec = tk.StringVar()
        self.section_fprimec_label = tk.Label(self.beam_props_frame, text="F'c (psi) : ", font=helv)
        self.section_fprimec_label.grid(row=0,column=2, pady=2)
        self.section_fprimec_entry = tk.Entry(self.beam_props_frame,textvariable=self.section_fprimec, font=helv, width=8)
        self.section_fprimec_entry.grid(row=0,column=3, pady=2)

        self.section_density = tk.StringVar()
        self.section_density_label = tk.Label(self.beam_props_frame, text="Concrete Density (pcf) :\n (90 to 160 pcf)", font=helv)
        self.section_density_label.grid(row=1,column=2, pady=2)
        self.section_density_entry = tk.Entry(self.beam_props_frame,textvariable=self.section_density, font=helv, width=8)
        self.section_density_entry.grid(row=1,column=3, pady=2)

        self.section_shear_bar = tk.StringVar()
        self.section_shear_bar_label = tk.Label(self.beam_props_frame, text="Shear Bar, Fy (ksi) :\n (up to 80 ksi)", font=helv)
        self.section_shear_bar_label.grid(row=2,column=2, pady=2)
        self.section_shear_bar_entry = tk.Entry(self.beam_props_frame,textvariable=self.section_shear_bar, font=helv, width=8)
        self.section_shear_bar_entry.grid(row=2,column=3, pady=2)

        self.section_shear_bar_size = tk.StringVar()
        self.section_shear_bar_size.set('3')
        self.section_shear_bar_size_label = tk.Label(self.beam_props_frame, text="Shear Bar Size (#) : ", font=helv)
        self.section_shear_bar_size_label.grid(row=3,column=2, pady=2)
        self.section_shear_bar_size_menu = tk.OptionMenu(self.beam_props_frame, self.section_shear_bar_size, '0','3', '4', '5','6','7','8','9','10','11','14','18', command=self.shear_bar_change)
        self.section_shear_bar_size_menu.config(font=helv)
        self.section_shear_bar_size_menu.grid(row=3, column=3, padx= 2, sticky=tk.W)

        self.section_flexural_bar = tk.StringVar()
        self.section_flexural_bar_label = tk.Label(self.beam_props_frame, text="Flexural Bars, Fy (ksi) :\n (up to 80 ksi)", font=helv)
        self.section_flexural_bar_label.grid(row=4,column=2, pady=2)
        self.section_flexural_bar_entry = tk.Entry(self.beam_props_frame,textvariable=self.section_flexural_bar, font=helv, width=8)
        self.section_flexural_bar_entry.grid(row=4,column=3, pady=2)

        self.b_section_create = tk.Button(self.beam_props_frame, text="Create Beam Section", command=self.create_section, font=helv)
        self.b_section_create.grid(row=9, column=1, padx=2, pady=2)
        
        self.beam_props_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.rebar_props_frame = tk.LabelFrame(self.frame_entry, text="Reinforcement", bd=1, relief='sunken', padx=2, pady=2)
        
        self.section_bottom_bar_label = tk.Label(self.rebar_props_frame, text="Add a Layer of Bars:", font=helv)
        self.section_bottom_bar_label.grid(row=10,column=1, pady=2)
        
        self.section_bottom_bar = tk.StringVar()
        self.section_bottom_bar_label = tk.Label(self.rebar_props_frame, text="Number of Bars :", font=helv)
        self.section_bottom_bar_label.grid(row=11,column=0, pady=2)
        self.section_bottom_bar_entry = tk.Entry(self.rebar_props_frame,textvariable=self.section_bottom_bar, state= "disabled", font=helv, width=8)
        self.section_bottom_bar_entry.grid(row=11,column=1, pady=2)
        
        self.section_bottom_bar_d = tk.StringVar()
        self.section_bottom_bar_d_label = tk.Label(self.rebar_props_frame, text="D (in):\nFrom Top", font=helv)
        self.section_bottom_bar_d_label.grid(row=12,column=0, pady=2)
        self.section_bottom_bar_d_entry = tk.Entry(self.rebar_props_frame,textvariable=self.section_bottom_bar_d, state= "disabled", font=helv, width=8)
        self.section_bottom_bar_d_entry.grid(row=12,column=1, pady=2)
        
        self.section_bottom_bar_size = tk.StringVar()
        self.section_bottom_bar_size.set('3')
        self.section_bottom_bar_size_label = tk.Label(self.rebar_props_frame, text="Bar Size (#) : ", font=helv)
        self.section_bottom_bar_size_label.grid(row=11,column=2, pady=2)
        self.section_bottom_bar_size_menu = tk.OptionMenu(self.rebar_props_frame, self.section_bottom_bar_size, '3', '4', '5','6','7','8','9','10','11','14','18', command=self.max_min_bars)
        self.section_bottom_bar_size_menu.config(font=helv)
        self.section_bottom_bar_size_menu.grid(row=11, column=3, padx= 2, sticky=tk.W)
        
        self.section_bottom_max_label = tk.Label(self.rebar_props_frame, text="Max of XX per Layer", font=helv)
        self.section_bottom_max_label.grid(row=13,column=1, pady=0)
        
        self.b_bottom_add = tk.Button(self.rebar_props_frame,text="Add", state= "disabled", command=self.add_bottom_bars, font=helv)
        self.b_bottom_change = tk.Button(self.rebar_props_frame, text="Change", state= "disabled", command = self.change_bottom_bars, font=helv)
        self.b_bottom_remove = tk.Button(self.rebar_props_frame, text="Remove", state= "disabled", command=self.remove_bottom_bars, font=helv)
                
        self.b_bottom_add.grid(row=14, column=0, padx=2, pady=2)
        self.b_bottom_change.grid(row=14, column=1, padx=2, pady=2)
        self.b_bottom_remove.grid(row=14, column=2, padx=2, pady=2)
        
        self.rebar_props_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.frame_entry.pack(side=tk.LEFT)
        ##Results Frame
        self.results_frame = tk.Frame(self.main_frame, bd=2, relief='sunken', padx=2, pady=2)
        ## Tables Frame
        self.tables_frame = tk.Frame(self.results_frame, bd=2, relief='sunken', padx=2, pady=2)
        ##bottom bars frame
        self.bottom_bars_frame = tk.LabelFrame(self.tables_frame, text="Bottom Bars", bd=1, relief='sunken', padx=2, pady=2, font=helv)
        
        self.bbsize_frame = tk.Frame(self.bottom_bars_frame)
        
        self.label_bottom_bar_size = tk.Label(self.bbsize_frame, text='Bar #', font=helv)
        self.label_bottom_bar_size.pack(side=tk.TOP)
        
        self.bottom_bars = tk.Listbox(self.bbsize_frame,height = 5, width = 10, font=helv)
        self.bottom_bars.pack(side=tk.TOP, fill=tk.Y, expand=True)
        self.bottom_bars.bind("<<ListboxSelect>>",self.bottom_bars_click)
        
        self.bbsize_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.bbcount_frame = tk.Frame(self.bottom_bars_frame)
        
        self.label_bottom_bar_number = tk.Label(self.bbcount_frame, text='Count', font=helv)
        self.label_bottom_bar_number.pack(side=tk.TOP)
        
        self.bottom_bars_count = tk.Listbox(self.bbcount_frame,height = 5, width = 10, bg= "grey90", font=helv)
        self.bottom_bars_count.pack(side=tk.TOP, fill=tk.Y, expand=1)
        
        self.bbcount_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.bbas_frame = tk.Frame(self.bottom_bars_frame)
        
        self.label_bottom_bar_area = tk.Label(self.bbas_frame, text='As (in^2)', font=helv)
        self.label_bottom_bar_area.pack(side=tk.TOP)
        
        self.bottom_bars_as = tk.Listbox(self.bbas_frame,height = 5, width = 10, bg= "grey90", font=helv)
        self.bottom_bars_as.pack(side=tk.TOP, fill=tk.Y, expand=True)
        
        self.bbas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.bbd_frame = tk.Frame(self.bottom_bars_frame)
        
        self.label_bottom_bar_d = tk.Label(self.bbd_frame, text='d (in)', font=helv)
        self.label_bottom_bar_d.pack(side=tk.TOP)
        self.bottom_bars_d = tk.Listbox(self.bbd_frame,height = 5, width = 10, bg= "grey90", font=helv)
        self.bottom_bars_d.pack(side=tk.TOP, fill=tk.Y, expand=True)
        
        self.bbd_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.bbstrain_frame = tk.Frame(self.bottom_bars_frame)
        self.label_bottom_bar_strain = tk.Label(self.bbstrain_frame, text='es (in)', font=helv)
        self.label_bottom_bar_strain.pack(side=tk.TOP)
        self.bottom_bars_strain = tk.Listbox(self.bbstrain_frame,height = 5, width = 10, bg= "grey90", font=helv)
        self.bottom_bars_strain.pack(side=tk.TOP, fill=tk.Y, expand=True)
        self.bbstrain_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.bbstress_frame = tk.Frame(self.bottom_bars_frame)
        self.label_bottom_bar_stress = tk.Label(self.bbstress_frame, text='fs (psi)', font=helv)
        self.label_bottom_bar_stress.pack(side=tk.TOP)
        self.bottom_bars_stress = tk.Listbox(self.bbstress_frame,height = 5, width = 10, bg= "grey90", font=helv)
        self.bottom_bars_stress.pack(side=tk.TOP, fill=tk.Y, expand=True)
        self.bbstress_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.bbforce_frame = tk.Frame(self.bottom_bars_frame)
        self.label_bottom_bar_force = tk.Label(self.bbforce_frame, text='Fs (lbs)', font=helv)
        self.label_bottom_bar_force.pack(side=tk.TOP)
        self.bottom_bars_axial = tk.Listbox(self.bbforce_frame,height = 5, width = 10, bg= "grey90", font=helv)
        self.bottom_bars_axial.pack(side=tk.TOP, fill=tk.Y, expand=True)
        self.bbforce_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.bbmoment_frame = tk.Frame(self.bottom_bars_frame)
        self.label_bottom_bar_moment = tk.Label(self.bbmoment_frame, text='Ms (ft-kips)', font=helv)
        self.label_bottom_bar_moment.pack(side=tk.TOP)
        
        self.bottom_bars_moment = tk.Listbox(self.bbmoment_frame,height = 5, width = 10, bg= "grey90", font=helv)
        self.bottom_bars_moment.pack(side=tk.TOP, fill=tk.Y, expand=True)
        self.bbmoment_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.bottom_bars_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.tables_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        ## Chart Frame
        self.chart_frame = tk.Frame(self.results_frame, padx=2, pady=2)
       
        
        self.x = [-5,5,5,-5,-5]
        self.y = [-5,-5,5,5,-5]
        
        self.Fig = matplotlib.figure.Figure(figsize=(2,2),dpi=100)
        self.FigSubPlot = self.Fig.add_subplot(111, aspect='equal', frameon = False)
        self.FigSubPlot.axis('off')
        
        self.section_graph, = self.FigSubPlot.plot(self.x,self.y,'r-')
        self.steel_centroid_graph, = self.FigSubPlot.plot(0,0,'bo')
        self.tension_steel_centroid_graph, = self.FigSubPlot.plot(0,1,'go')
        self.pna_graph, = self.FigSubPlot.plot(0,3,'m+')
        self.cc_graph, = self.FigSubPlot.plot(0,4,'r+')
        self.steel_cg_graph_label = self.FigSubPlot.annotate('(Steel CG: {0:.2f} in.)'.format(0,0),xy=(0,0), xytext=(5,-5), ha='left',textcoords='offset points', fontsize=8)
        self.tension_steel_cg_graph_label = self.FigSubPlot.annotate('(Tension Steel CG: {0:.2f} in.)'.format(0,1),xy=(0,1), xytext=(5,-5), ha='left',textcoords='offset points', fontsize=8)
        self.pna_graph_label = self.FigSubPlot.annotate('(PNA: {0:.2f} in.)'.format(0,3),xy=(0,3), xytext=(5,-5), ha='left',textcoords='offset points', fontsize=8)
        self.cc_graph_label = self.FigSubPlot.annotate('(a,cg: {0:.2f} in.)'.format(0,4),xy=(0,4), xytext=(5,-5), ha='left',textcoords='offset points', fontsize=8)
        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.Fig, master=self.chart_frame)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.chart_toolbar = NavigationToolbar2TkAgg(self.canvas, self.chart_frame)
        self.chart_toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.chart_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.results_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        ## Text Results Frame
        self.text_results_frame = tk.LabelFrame(self.main_frame, text="Concrete Section and Overall Results", bd=2, relief='sunken', padx=2, pady=2, font=helv)
        
        self.results_text_box = tk.Text(self.text_results_frame, height = 10, width = 10, bg= "grey90", font= tkFont.Font(family='Helvetica',size=8, weight='normal'), wrap=tk.WORD)
        self.results_text_box.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.text_results_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       
        ## Outside Main Frame
        self.b1 = tk.Button(master,text="Close", command=self.quit_app, font=helv)
        self.b1.pack(side=tk.RIGHT, padx=5, pady=5)        
    
        self.brun = tk.Button(master, text="Run", command= self.run_file, font=helv)
        self.brun.configure(state="disabled")
        self.brun.pack(side=tk.RIGHT, padx=5, pady=5)
        self.label_error = tk.Label(master, text='Error Info if Any', font=helv)
        self.label_error.pack(side=tk.LEFT)
        
        self.section_created = 0
        self.error_check = 0
        
    def quit_app(self):
        self.master.destroy()
        self.master.quit()
    
    def create_section(self):
        self.inputs=[]
        self.t_inputs = []
        self.error_check = 0
        
        #Gather cross section inputs
        self.inputs.append(self.section_b.get())
        self.inputs.append(self.section_h.get())
        self.inputs.append(self.section_cover.get())
        self.inputs.append(self.section_agg.get())
        self.inputs.append(self.section_fprimec.get())
        self.inputs.append(self.section_density.get())
        self.inputs.append(self.section_shear_bar.get())
        self.inputs.append(self.section_shear_bar_size.get())
        self.inputs.append(self.section_flexural_bar.get())
        
        #Gather Flange information
        if self.section_span.get() == '':
            self.t_inputs.append(0)
        else:
            self.t_inputs.append(float(self.section_span.get()))
        
        if self.section_slab_thickness.get() == '':
            self.t_inputs.append(0)
        else:
            self.t_inputs.append(float(self.section_slab_thickness.get()))
        
        if self.section_span_slab_left.get() == '':
            self.t_inputs.append(0)
        else:
            self.t_inputs.append(float(self.section_span_slab_left.get()))
        
        if self.section_span_slab_right.get() == '':
            self.t_inputs.append(0)
        else:
            self.t_inputs.append(float(self.section_span_slab_right.get()))
        
        if self.section_bf.get() == '':
            self.t_inputs.append(0)
        else:
            self.t_inputs.append(float(self.section_bf.get()))
        
        if self.section_hf.get() == '':
            self.t_inputs.append(0)
        else:
            self.t_inputs.append(float(self.section_hf.get()))
        
        if self.t_inputs[4] != 0 and self.t_inputs[2] != 0:
            self.label_error.configure(text = 'Error! : Either Provide the flange width or provide Span information to calculate span width, do not do both')
            self.error_check = 1
        else:
            pass
        
        for inputs in self.inputs:
            if inputs == 0 or inputs == '':
                self.label_error.configure(text = 'Error! : Must Provide all Beam Section Inputs to Create Section')
                self.error_check = 1
            else:
                pass
        
        if self.error_check == 1:
            pass
        else:
            self.section_created = 1

            self.results_text_box.delete(1.0,tk.END)
            self.clear_bar_res_lists()

            self.b_in = float(self.inputs[0])
            self.h_in = float(self.inputs[1])
            self.cover_in = float(self.inputs[2])
            self.aggregate_size_in = float(self.inputs[3])
            self.fprimec_psi = float(self.inputs[4])
            self.density_pcf = float(self.inputs[5])
            self.shear_bars_fy_psi = float(self.inputs[6])
            self.shear_bar_size = int(self.inputs[7])
            self.flexural_bars_fy_psi = float(self.inputs[8])
            
            self.beamsection = concbeam.t_beam(self.b_in,self.h_in,self.t_inputs[1],self.t_inputs[0],self.t_inputs[2],self.t_inputs[3],self.t_inputs[4],self.t_inputs[5],self.fprimec_psi,self.density_pcf)
            self.shear_bars_fy = concbeam.reinforcement(self.shear_bars_fy_psi)
            self.shear_bar = self.shear_bars_fy.bar[self.shear_bar_size]
            self.flexural_bars_fy = concbeam.reinforcement(self.flexural_bars_fy_psi)
            
            self.max_min_bars()
            

            self.b_bottom_add.configure(state= "normal")
            self.b_bottom_change.configure(state= "disabled")
            self.b_bottom_remove.configure(state= "normal")
            self.section_bottom_bar_entry.configure(state= "normal")
            self.section_bottom_bar_d_entry.configure(state="normal")
            
            self.line1 = 'I gross = {0:.2f} in^4\nEc = {1:0.2f} psi = {2:0.2f} ksi\nSelf Wt = {3:0.2f} plf = {4:0.2f} klf'.format(self.beamsection.Ig_in4,self.beamsection.Ec_psi,self.beamsection.Ec_psi/1000, self.beamsection.weight_plf,self.beamsection.weight_klf)
            self.line2 = '\nFr = {0:.2f} psi\nCracking Moment, Mcr = {1:0.2f} in-lbs = {2:0.2f} ft-lbs = {3:0.2f} ft-kips'.format(self.beamsection.fr_psi,self.beamsection.Mcrack_inlbs,self.beamsection.Mcrack_ftlbs,self.beamsection.Mcrack_ftkips)
            self.results_text_box.insert(tk.END, self.line1)
            self.results_text_box.insert(tk.END, self.line2)
            
            x = self.beamsection.section_x_coords_in
            y = self.beamsection.section_y_coords_in
            
            self.section_graph.set_data(x,y)
            ax = self.canvas.figure.axes[0]
            ax.set_xlim(min(x)-2, max(x)+2)
            ax.set_ylim(min(y)-2, max(y)+2)
            
           
            self.canvas.draw()
            
            
            self.t_beam_flange_frame.configure(text='T Beam Flange Properties:\n Bf: {0:0.3f} in -- Hf: {1:0.3f} in -- B,lo: {2:0.3f} in -- B,ro: {3:0.3f} in\nStatus: {4}'.format(self.beamsection.bf_in, self.beamsection.hf_in, self.beamsection.bf_left_in,self.beamsection.bf_right_in, self.beamsection.bf_status))
            if self.beamsection.bf_status != 'OK':
                self.label_error.configure(text ='{0}'.format(self.beamsection.bf_status))
            else:
                self.label_error.configure(text ='Section Creation OK')
                
    def max_min_bars(self, *kwargs):
        if self.section_created == 1:
            self.bottom_bar_size = int(self.section_bottom_bar_size.get())
            
            self.bottom_bar = self.flexural_bars_fy.bar[self.bottom_bar_size]
            
            self.min_outer_bars = self.beamsection.min_bars_bottom_layer(self.bottom_bar,self.cover_in,self.shear_bar, self.flexural_bars_fy.fy_psi)
            self.max_bottom_bars_per_Layer = self.beamsection.max_bars_layer(self.bottom_bar,self.cover_in,self.shear_bar, self.aggregate_size_in)
            
            self.section_bottom_max_label.configure(text = 'Min of {0} Bars in Bottom Most Layer\nMax of {1} Bars per Layer'.format(self.min_outer_bars, self.max_bottom_bars_per_Layer))
        else:
            pass
    
    def add_bottom_bars(self):
        if self.section_created == 1:
            number_of_bars = self.section_bottom_bar.get()
            d = self.section_bottom_bar_d.get()
            if number_of_bars == '':
                self.label_error.configure(text = 'Error! : Enter number of bottom bars')
                self.error_check = 1
            else:
                number_of_bars = float(self.section_bottom_bar.get())
                self.error_check = 0
            
            if d == '':
                self.label_error.configure(text = 'Error! : Enter d for bar layer')
                self.error_check = 1
            elif float(d) > self.beamsection.h_in or float(d) < 0:
                self.label_error.configure(text = 'Error! : Enter value of d that is within the cross section depth')
                self.error_check = 1
            else:
                self.bottom_bars.insert(tk.END,self.section_bottom_bar_size.get())
                self.bottom_bars_count.insert(tk.END,self.section_bottom_bar.get())
                self.bottom_bars_d.insert(tk.END,self.section_bottom_bar_d.get())
                bar_as = self.flexural_bars_fy.bar[int(self.section_bottom_bar_size.get())][1] * float(self.section_bottom_bar.get())
                bar_as_string = '{0:0.5f}'.format(bar_as)
                self.bottom_bars_as.insert(tk.END,bar_as_string)
                self.brun.configure(state="normal")
                self.clear_bar_res_lists()
                self.error_check = 0
                self.run_file()
        else:
            pass
    def remove_bottom_bars(self):
        self.bottom_bars.delete(tk.END)
        self.bottom_bars_count.delete(tk.END)
        self.bottom_bars_d.delete(tk.END)
        self.bottom_bars_as.delete(tk.END)
        self.clear_bar_res_lists()
        
        if self.bottom_bars.size()==0:
            self.brun.configure(state="disabled")
            self.b_bottom_change.configure(state= "disable")
            self.error_check = 0
        else:
            self.brun.configure(state="normal")
            self.b_bottom_change.configure(state= "disable")
            self.error_check = 0
            self.run_file()
            
    def bottom_bars_click(self,*event):
        pass
        if self.bottom_bars.size()==0:
            pass
        else:
            self.b_bottom_change.configure(state= "normal")
            self.bottom_change_index = self.bottom_bars.curselection()[0]

    def change_bottom_bars(self):
        if self.section_created == 1:
            number_of_bars = self.section_bottom_bar.get()
            d = self.section_bottom_bar_d.get()
            if number_of_bars == '':
                self.label_error.configure(text = 'Error! : Enter number of bottom bars')
                self.error_check = 1
            else:
                number_of_bars = float(self.section_bottom_bar.get())
                self.error_check = 0
            
            if d == '':
                self.label_error.configure(text = 'Error! : Enter d for bar layer')
                self.error_check = 1
            elif float(d) > self.beamsection.h_in or float(d) < 0:
                self.label_error.configure(text = 'Error! : Enter value of d that is within the cross section depth')
                self.error_check = 1
            else:
                self.bottom_bars.delete(self.bottom_change_index)
                self.bottom_bars_count.delete(self.bottom_change_index)
                self.bottom_bars_d.delete(self.bottom_change_index)
                self.bottom_bars_as.delete(self.bottom_change_index)
                self.bottom_bars.insert(self.bottom_change_index,self.section_bottom_bar_size.get())
                self.bottom_bars_count.insert(self.bottom_change_index,self.section_bottom_bar.get())
                self.bottom_bars_d.insert(self.bottom_change_index,self.section_bottom_bar_d.get())
                bar_as = self.flexural_bars_fy.bar[int(self.section_bottom_bar_size.get())][1] * float(self.section_bottom_bar.get())
                bar_as_string = '{0:0.5f}'.format(bar_as)
                self.bottom_bars_as.insert(self.bottom_change_index,bar_as_string)
                self.brun.configure(state="normal")
                self.b_bottom_change.configure(state= "disable")
                self.clear_bar_res_lists()
                self.error_check = 0
                self.run_file()
        else:
            pass
    
    def shear_bar_change(self, *kwargs):
        self.error_check = 0
        
        if self.section_created == 1:
            
            self.shear_bar_size = int(self.section_shear_bar_size.get())
            self.shear_bar = self.shear_bars_fy.bar[self.shear_bar_size]
            
            self.max_min_bars()
            self.clear_bar_res_lists()

        else:
            pass
    def clear_bar_res_lists(self, *kwargs):
            self.bottom_bars_strain.delete(0,tk.END)
            self.bottom_bars_stress.delete(0,tk.END)
            self.bottom_bars_axial.delete(0,tk.END) 
            self.bottom_bars_moment.delete(0,tk.END)

    def run_file(self):
        
        self.results_text_box.delete(1.0,tk.END)
        self.results_text_box.insert(tk.END, self.line1)
        self.results_text_box.insert(tk.END, self.line2)
        self.clear_bar_res_lists()
        
        if self.error_check == 1:
            pass
        else:
            bottom_bars_array = []
            bottom_bars_per_layer_array = []
            bottom_bars_d_array = []
            bottom_bars_as_array = []
            top_bars_array = []
            top_bars_per_layer_array = []
            flexural_bars_array = []
            flexural_bars_as_array = []
            flexural_bars_d_array = []
            
            bottom_bars_moment_ftkips_array = []

            top_bars_moment_ftkips_array = []
            
            flexural_bars_cg = 0
            
            fy_psi = self.flexural_bars_fy.fy_psi
            Es_psi = self.flexural_bars_fy.Es_psi
            
            bottom_bars_raw = self.bottom_bars.get(0,tk.END)
            bottom_bars_d_raw = self.bottom_bars_d.get(0,tk.END)
            bottom_bars_as_raw = self.bottom_bars_as.get(0,tk.END)
            
            for line in bottom_bars_raw:            
                flexural_bars_array.append(self.flexural_bars_fy.bar[int(line)])
            for line in bottom_bars_d_raw:            
                flexural_bars_d_array.append(float(line))
            for line in bottom_bars_as_raw:
                flexural_bars_as_array.append(float(line))
            
            total_as = sum(flexural_bars_as_array)
            total_as_d = 0
            i=0
            for i in range(len(flexural_bars_as_array)):
                total_as_d = total_as_d + (flexural_bars_as_array[i]*flexural_bars_d_array[i])

            flexural_bars_cg = total_as_d/total_as
            
            self.steel_centroid_graph.set_data(self.b_in/2,self.h_in - flexural_bars_cg)
            self.steel_cg_graph_label.remove()
            self.steel_cg_graph_label = self.FigSubPlot.annotate('(Steel CG: {0:.3f} in.)'.format(flexural_bars_cg),xy=(self.b_in/2,self.h_in - flexural_bars_cg), xytext=(0,5), ha='center',textcoords='offset points', fontsize=8)           
            self.PNA = self.beamsection.find_pna(flexural_bars_as_array,flexural_bars_d_array,flexural_bars_cg,fy_psi,Es_psi)
            self.pna_graph.set_data(self.b_in/2,self.h_in - self.PNA)
            self.pna_graph_label.remove()
            self.pna_graph_label = self.FigSubPlot.annotate('(PNA: {0:.3f} in.)'.format(self.PNA),xy=(self.b_in/2,self.h_in - self.PNA), xytext=(0,-10), ha='center',textcoords='offset points', fontsize=8)
            self.canvas.draw()
            
            bottom_bars_strain_array, bottom_bars_stress_psi_array, bottom_bars_force_lbs_array, total_bottom_force = self.beamsection.strain_compatibility_steel(flexural_bars_as_array,flexural_bars_d_array,self.PNA,fy_psi,Es_psi)
            
            i=0
            for i in range(len(bottom_bars_strain_array)):
                self.bottom_bars_strain.insert(tk.END,'{0:0.6f}'.format(bottom_bars_strain_array[i]))
                self.bottom_bars_stress.insert(tk.END,'{0:0.3f}'.format(bottom_bars_stress_psi_array[i]))
                self.bottom_bars_axial.insert(tk.END,'{0:0.3f}'.format(bottom_bars_force_lbs_array[i])) 
                self.bottom_bars_moment.insert(tk.END,'{0:0.3f}'.format((bottom_bars_force_lbs_array[i]*(flexural_bars_d_array[i]-flexural_bars_cg))/(12*1000)))
                
                if bottom_bars_strain_array[i] >=0:
                    bottom_bars_as_array.append(flexural_bars_as_array[i])
                    bottom_bars_d_array.append(flexural_bars_d_array[i])

                else:
                    pass
        
            total_as_tension = sum(bottom_bars_as_array)
            total_as_d_tension = 0
            i=0
            for i in range(len(bottom_bars_as_array)):
                total_as_d_tension = total_as_d_tension + (bottom_bars_as_array[i]*bottom_bars_d_array[i])

            bottom_bars_cg = total_as_d_tension/total_as_tension
            
            self.tension_steel_centroid_graph.set_data(self.b_in/2,self.h_in - bottom_bars_cg)
            self.tension_steel_cg_graph_label.remove()
            self.tension_steel_cg_graph_label = self.FigSubPlot.annotate('(Tension Steel CG: {0:.3f} in.)'.format(bottom_bars_cg),xy=(self.b_in/2,self.h_in - bottom_bars_cg), xytext=(0,-10), ha='center',textcoords='offset points', fontsize=8)           

            self.minas = self.beamsection.as_min(bottom_bars_cg,fy_psi)
            if self.minas <= sum(bottom_bars_as_array):
                status = 'OK'
            else:
                status = 'NG'
            self.bottom_bars_frame.configure(text='Flexural Bars - As,min: {0:0.3f} in^2 -- As,actual: {1:0.3f} in^2 --{2}'.format(self.minas,sum(bottom_bars_as_array),status))
            
            concrete_compression_force_lbs, concrete_compression_force_cg_in = self.beamsection.strain_compatibility_concrete(self.PNA)
            
            if 1 - (abs(concrete_compression_force_lbs) / abs(total_bottom_force)) <= 0.00001:
                status_force = 'OK'
            else:
                status_force = 'NG'
            self.text_results_frame.configure(text='Concrete Section and Overall Results - Cc: {0:0.3f} kips -- Ts: {1:0.3f} kips --{2}'.format(concrete_compression_force_lbs/1000,(total_bottom_force)/1000,status_force))  

            if max(bottom_bars_strain_array)<0.004:
                self.label_error.configure(text = 'Error! : Section not Tension Controlled')
                self.line3 = '\n\n\n ERROR!! -- SECTION NOT TENSION CONTROLLED'
                self.results_text_box.delete(1.0,tk.END)
                self.results_text_box.insert(tk.END, self.line1)
                self.results_text_box.insert(tk.END, self.line2)
                self.results_text_box.insert(tk.END, self.line3)
                self.error_check = 1
            else:
                phi, nominal_moment, ultimate_moment = self.beamsection.moment_capacity_inlbs(flexural_bars_as_array,flexural_bars_d_array,flexural_bars_cg,self.PNA,fy_psi,Es_psi) 
                    
                phiv, vc, phivc, vsmax, vnmax, phivnmax = self.beamsection.concrete_shear_capacity_lbs(bottom_bars_cg,self.shear_bars_fy.fy_psi,self.shear_bar[1])
                phit, Acp, Pcp, t_threshold, phit_threshold, aop_status = self.beamsection.concrete_threshold_torsion_inlbs()
                
                a = self.beamsection.beta1 * self.PNA
                self.cc_graph.set_data(self.b_in/2,self.h_in - (concrete_compression_force_cg_in))
                self.cc_graph_label.remove()
                self.cc_graph_label = self.FigSubPlot.annotate('(a,cg: {0:.3f} in.)'.format(concrete_compression_force_cg_in),xy=(self.b_in/2,self.h_in - (concrete_compression_force_cg_in)), xytext=(0,5), ha='center',textcoords='offset points', fontsize=8)
                self.canvas.draw()
                
                self.line3 = '\n\nC,PNA = {0:.4f} * beta1 = {1:.3f} = a = {2:.4f} in'.format(self.PNA,self.beamsection.beta1,a)
            
                self.line4 = '\n\nFLEXURE:\n\n Phi = {0:.3f}    Mn = {1:.3f} in-lbs = {2:.3f} ft-lbs = {3:.3f} ft-kips\n Phi*Mn =  {4:.3f} in-lbs = {5:.3f} ft-lbs = {6:.3f} ft-kips'.format(phi,nominal_moment,nominal_moment/12,nominal_moment/(12*1000),ultimate_moment,ultimate_moment/12,ultimate_moment/(12*1000))
                self.line5 = '\n\nSHEAR:\n\n Phi = {0:.3f}\n Vc = {1:.3f} lbs = {2:.3f} kips\n Phi*Vc = {3:.3f} lbs = {4:.3f} kips\n 0.5*Phi*Vc = {11:.3f} lbs = {12:.3f} kips\n Vs,max = {5:.3f} lbs = {6:.3f} kips\n Vn,max = Vc + Vs,max = {7:.3f} lbs = {8:.3f} kips\n Phi*Vn,max = {9:.3f} lbs = {10:.3f} kips'.format(phiv, vc, vc/1000,phivc, phivc/1000,vsmax,vsmax/1000,vnmax,vnmax/1000,phivnmax,phivnmax/1000,0.5*phivc, 0.5*phivc/1000)
                self.line6 = '\n\nSHEAR REINFORCEMENT:\n\n Max Spacing : {0:.3f} in\n Max Spacing if Vs,req = 0.5*Vs,max : {9:.3f} in\n --s = spacing in inches--\n Av,min = {1:.3f} * s in^2 = {2:.3f} in^2 @ max spacing\n 2-VERT LEGS:\n Vs = {3:.3f} / s * (1 kip/1000 lbs) = {4:.3f} kips @ max spacing\n 4-VERT LEGS:\n Vs = {5:.3f} / s * (1 kip/1000 lbs) = {6:.3f} kips @ max spacing\n 6-VERT LEGS:\n Vs = {7:.3f} / s * (1 kip/1000 lbs) = {8:.3f} kips @ max spacing'.format(self.beamsection.max_shear_spacing_in,self.beamsection.av_min_s,self.beamsection.max_shear_spacing_in*self.beamsection.av_min_s,self.beamsection.s_Vs_2_legs,(self.beamsection.s_Vs_2_legs/self.beamsection.max_shear_spacing_in)/1000,self.beamsection.s_Vs_4_legs,(self.beamsection.s_Vs_4_legs/self.beamsection.max_shear_spacing_in)/1000,self.beamsection.s_Vs_6_legs,(self.beamsection.s_Vs_6_legs/self.beamsection.max_shear_spacing_in)/1000,0.5*self.beamsection.max_shear_spacing_in)
                self.line7 = '\n\nTHRESHOLD TORSION:\n\n Phi = {0:.3f}\n Acp = {1:.3f} in^2 \n Pcp = {2:.3f} in \n {3} \n Tu,threshold = {4:.3f} in-lbs = {5:.3f} ft-lbs = {6:.3f} ft-kips \n Phi*Tu,threshold = {7:.3f} in-lbs = {8:.3f} ft-lbs = {9:.3f} ft-kips'.format(phit, Acp, Pcp, aop_status, t_threshold, t_threshold/12.0, t_threshold/(12.0*1000), phit_threshold, phit_threshold/12.0, phit_threshold/(12.0*1000))
                
                i_cracked_in4 = self.beamsection.cracked_moment_of_inertia_in4(flexural_bars_as_array,flexural_bars_d_array,Es_psi)
                self.line2 = '\nFr = {0:.2f} psi\nCracking Moment, Mcr = {1:0.2f} in-lbs = {2:0.2f} ft-lbs = {3:0.2f} ft-kips\nI cracked = {4:0.3f} in^4'.format(self.beamsection.fr_psi,self.beamsection.Mcrack_inlbs,self.beamsection.Mcrack_ftlbs,self.beamsection.Mcrack_ftkips,i_cracked_in4)
                
                if self.error_check == 1:
                    self.results_text_box.delete(1.0,tk.END)
                    self.results_text_box.insert(tk.END, self.line1)
                    self.results_text_box.insert(tk.END, self.line2)
                    self.results_text_box.insert(tk.END, self.line3)
                else:
                    self.results_text_box.delete(1.0,tk.END)
                    self.results_text_box.insert(tk.END, self.line1)
                    self.results_text_box.insert(tk.END, self.line2)
                    self.results_text_box.insert(tk.END, self.line3)
                    self.results_text_box.insert(tk.END, self.line4)
                    self.results_text_box.insert(tk.END, self.line5)
                    self.results_text_box.insert(tk.END, self.line6)
                    self.results_text_box.insert(tk.END, self.line7)
                    self.label_error.configure(text ='Section Analysis Complete')
def main(): 
    root = tk.Tk()
    root.title("Concrete T Beam - User Steel Elevations")
    app = Main_window(root)
    root.minsize(width=1230, height=720)
    root.mainloop()

if __name__ == '__main__':
    main()

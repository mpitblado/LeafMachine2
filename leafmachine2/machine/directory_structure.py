import os, pathlib, sys, inspect
from dataclasses import dataclass, field
currentdir = os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append(currentdir)
from leafmachine2.machine.general_utils import validate_dir, get_datetime

@dataclass
class Dir_Structure():
    # Home 
    run_name: str = ''
    dir_home: str = ''
    dir_project: str = ''

    # Processing dirs
    path_plant_components: str = ''
    path_archival_components: str = ''
    path_config_file: str = ''

    whole_leaves: str = ''
    partial_leaves: str = ''

    segmentation_overlay_pdfs: str = ''
    segmentation_whole_leaves: str = ''
    segmentation_partial_leaves: str = ''

    segmentation_masks_color_whole_leaves: str = ''
    segmentation_masks_color_partial_leaves: str = ''

    segmentation_overlay_whole_leaves: str = ''
    segmentation_overlay_partial_leaves: str = ''

    segmentation_masks_full_image_color_whole_leaves: str = ''
    segmentation_masks_full_image_color_partial_leaves: str = ''

    ruler_info: str = ''
    ruler_overlay: str = ''
    ruler_processed: str = ''
    ruler_data: str = ''
    ruler_class_overlay: str = ''
    ruler_validation_summary: str = ''
    ruler_validation: str = ''

    data_csv_project_ruler: str = ''
    data_csv_project_batch_ruler: str = ''
    data_csv_project_measurements: str = ''
    data_csv_project_batch_measurements: str = ''

    data_csv_individual_rulers: str = ''
    data_csv_individual_measurements: str = ''
    data_json_rulers: str = ''
    data_json_measurements: str = ''

    dir_images_subset: str = ''

    save_per_image: str = ''
    save_per_annotation_class: str = ''
    binarize_labels: str = ''

    # landmarks
    landmarks: str = ''
    landmarks_whole_leaves_overlay: str = ''
    landmarks_partial_leaves_overlay: str = ''

    # logging
    path_log: str = ''
    
    def __init__(self, cfg) -> None:
        # Home 
        self.run_name = cfg['leafmachine']['project']['run_name']
        self.dir_home = cfg['leafmachine']['project']['dir_output']
        self.dir_project = os.path.join(self.dir_home,self.run_name)
        validate_dir(self.dir_home)
        self.__add_time_to_existing_project_dir()
        validate_dir(self.dir_project)

        # Processing dirs
        self.path_plant_components = os.path.join(self.dir_project,'Plant_Components')
        self.path_archival_components = os.path.join(self.dir_project,'Archival_Components')
        self.path_config_file = os.path.join(self.dir_project,'Config_File')
        validate_dir(self.path_config_file)

        # Logging
        self.path_log = os.path.join(self.dir_project,'Logs')
        validate_dir(self.path_log)

        self.segmentation_overlay_pdfs = os.path.join(self.dir_project,'Plant_Components','Segmentation_Overlay_PDFs')

        self.custom_overlay_pdfs = os.path.join(self.dir_project,'Summary','Custom_Overlay_PDFs')
        self.custom_overlay_images = os.path.join(self.dir_project,'Summary','Custom_Overlay_Images')

        ###
        self.custom_overlay_pdfs = os.path.join(self.dir_project,'Summary','Custom_Overlay_PDFs')
        if cfg['leafmachine']['overlay']['save_overlay_to_pdf']:
            validate_dir(self.custom_overlay_pdfs)

        self.custom_overlay_images = os.path.join(self.dir_project,'Summary','Custom_Overlay_Images')
        if cfg['leafmachine']['overlay']['save_overlay_to_jpgs']:
            validate_dir(self.custom_overlay_images)

        ### Cropped images
        self.whole_leaves = os.path.join(self.dir_project,'Plant_Components','Leaves_Whole')
        self.partial_leaves = os.path.join(self.dir_project,'Plant_Components','Leaves_Partial')
        if cfg['leafmachine']['leaf_segmentation']['save_rgb_cropped_images']:
            validate_dir(self.whole_leaves)
            validate_dir(self.partial_leaves)

        ### Segmentation overlay
        self.segmentation_whole_leaves = os.path.join(self.dir_project,'Plant_Components','Segmentation_Whole_Leaves')
        self.segmentation_partial_leaves = os.path.join(self.dir_project,'Plant_Components','Segmentation_Partial_Leaves')
        if cfg['leafmachine']['leaf_segmentation']['save_individual_overlay_images']:
            validate_dir(self.segmentation_whole_leaves)
            validate_dir(self.segmentation_partial_leaves)
        ### Cropped Masks
        self.segmentation_masks_color_whole_leaves = os.path.join(self.dir_project,'Plant_Components','Segmentation_Masks_Color_Whole_Leaves')
        self.segmentation_masks_color_partial_leaves = os.path.join(self.dir_project,'Plant_Components','Segmentation_Masks_Color_Partial_Leaves')
        if cfg['leafmachine']['leaf_segmentation']['save_masks_color']:
            validate_dir(self.segmentation_masks_color_whole_leaves)
            validate_dir(self.segmentation_masks_color_partial_leaves)

        self.segmentation_overlay_whole_leaves = os.path.join(self.dir_project,'Plant_Components','Segmentation_Overlay_Whole_Leaves')
        self.segmentation_overlay_partial_leaves = os.path.join(self.dir_project,'Plant_Components','Segmentation_Overlay_Partial_Leaves')
        if cfg['leafmachine']['leaf_segmentation']['save_each_segmentation_overlay_image']:
            validate_dir(self.segmentation_overlay_whole_leaves)
            validate_dir(self.segmentation_overlay_partial_leaves)

        ### Full Image Masks
        self.segmentation_masks_full_image_color_whole_leaves = os.path.join(self.dir_project,'Plant_Components','Segmentation_Masks_Full_Image_Color_Whole_Leaves')
        self.segmentation_masks_full_image_color_partial_leaves = os.path.join(self.dir_project,'Plant_Components','Segmentation_Masks_Full_Image_Color_Partial_Leaves')
        if cfg['leafmachine']['leaf_segmentation']['save_full_image_masks_color']:
            validate_dir(self.segmentation_masks_full_image_color_whole_leaves)
            validate_dir(self.segmentation_masks_full_image_color_partial_leaves)        

        ### Rulers
        self.ruler_info = os.path.join(self.dir_project,'Archival_Components','Ruler_Info')  
        self.ruler_validation_summary =  os.path.join(self.dir_project,'Archival_Components','Ruler_Info', 'Ruler_Validation_Summary')
        self.ruler_validation = os.path.join(self.dir_project,'Archival_Components','Ruler_Info', 'Ruler_Validation')
        self.ruler_processed = os.path.join(self.dir_project,'Archival_Components','Ruler_Info', 'Ruler_Processed')
        validate_dir(self.ruler_info)
        if cfg['leafmachine']['ruler_detection']['save_ruler_validation_summary']:
            validate_dir(self.ruler_validation_summary)
        if cfg['leafmachine']['ruler_detection']['save_ruler_validation']:
            validate_dir(self.ruler_validation)

            validate_dir(self.ruler_processed)
            # validate_dir(self.ruler_data)


        validate_dir(self.path_plant_components)
        validate_dir(os.path.join(self.path_plant_components, 'JSON'))
        validate_dir(os.path.join(self.segmentation_overlay_pdfs))

        validate_dir(self.path_archival_components)
        validate_dir(os.path.join(self.path_archival_components, 'JSON'))


        ### Data
        self.data_csv_project_ruler = os.path.join(self.dir_project,'Data','Ruler') 
        validate_dir(self.data_csv_project_ruler)
        self.data_csv_project_batch_ruler = os.path.join(self.dir_project,'Data','Batch','Ruler') 
        validate_dir(self.data_csv_project_batch_ruler)

        self.data_csv_project_measurements = os.path.join(self.dir_project,'Data','Measurements') 
        validate_dir(self.data_csv_project_measurements)
        self.data_csv_project_batch_measurements = os.path.join(self.dir_project,'Data','Batch','Measurements') 
        validate_dir(self.data_csv_project_batch_measurements)

        self.data_csv_project_EFD = os.path.join(self.dir_project,'Data','EFD') 
        self.data_csv_project_batch_EFD = os.path.join(self.dir_project,'Data','Batch','EFD') 
        if cfg['leafmachine']['leaf_segmentation']['calculate_elliptic_fourier_descriptors']:
            validate_dir(self.data_csv_project_EFD)
            validate_dir(self.data_csv_project_batch_EFD)

        self.data_csv_individual_rulers = os.path.join(self.dir_project,'Data', 'CSV', 'Rulers') 
        self.data_json_rulers = os.path.join(self.dir_project,'Data', 'JSON', 'Rulers') 
        if cfg['leafmachine']['data']['save_json_rulers']:
            validate_dir(self.data_json_rulers)
        if cfg['leafmachine']['data']['save_individual_csv_files_rulers']:
            validate_dir(self.data_csv_individual_rulers)

        self.data_csv_individual_measurements = os.path.join(self.dir_project,'Data', 'CSV', 'Measurements') 
        self.data_json_measurements = os.path.join(self.dir_project,'Data', 'JSON', 'Measurements') 
        if cfg['leafmachine']['data']['save_json_measurements']:
            validate_dir(self.data_json_measurements)
        if cfg['leafmachine']['data']['save_individual_csv_files_measurements']:
            validate_dir(self.data_csv_individual_measurements)


        self.dir_images_subset = os.path.join(self.dir_project,'Subset') 
        if cfg['leafmachine']['project']['process_subset_of_images']:
            validate_dir(self.dir_images_subset)

        self.save_per_image = os.path.join(self.dir_project,'Cropped_Images', 'By_Image') 
        self.save_per_annotation_class = os.path.join(self.dir_project,'Cropped_Images', 'By_Class') 
        self.save_per_annotation_class = os.path.join(self.dir_project,'Cropped_Images', 'By_Class') 
        if cfg['leafmachine']['cropped_components']['save_per_image']:
            validate_dir(self.save_per_image)
        if cfg['leafmachine']['cropped_components']['save_per_annotation_class']:
            validate_dir(self.save_per_annotation_class)
        if cfg['leafmachine']['cropped_components']['binarize_labels']:
            validate_dir(self.save_per_annotation_class)
            # self.binarize_labels = os.path.join(self.dir_project,'Cropped_Images', 'By_Class','label_binary') 
            # validate_dir(self.binarize_labels)

        '''Landmarks'''
        self.landmarks = os.path.join(self.dir_project,'Plant_Components','Landmarks')
        validate_dir(self.landmarks)

        self.landmarks_whole_leaves_overlay = os.path.join(self.dir_project,'Plant_Components','Landmarks_Whole_Leaves_Overlay')
        self.landmarks_partial_leaves_overlay = os.path.join(self.dir_project,'Plant_Components','Landmarks_Partial_Leaves_Overlay')
        if cfg['leafmachine']['landmark_detector']['do_save_prediction_overlay_images']:
            validate_dir(self.landmarks_whole_leaves_overlay)
            validate_dir(self.landmarks_partial_leaves_overlay)

        self.landmarks_whole_leaves_overlay_QC = os.path.join(self.dir_project,'Plant_Components','Landmarks_Whole_Leaves_Overlay_QC')
        self.landmarks_partial_leaves_overlay_QC = os.path.join(self.dir_project,'Plant_Components','Landmarks_Partial_Leaves_Overlay_QC')
        if cfg['leafmachine']['landmark_detector']['do_save_QC_images']:
            validate_dir(self.landmarks_whole_leaves_overlay_QC)
            validate_dir(self.landmarks_partial_leaves_overlay_QC)

        self.landmarks_whole_leaves_overlay_final = os.path.join(self.dir_project,'Plant_Components','Landmarks_Whole_Leaves_Overlay_Final')
        self.landmarks_partial_leaves_overlay_final = os.path.join(self.dir_project,'Plant_Components','Landmarks_Partial_Leaves_Overlay_Final')
        if cfg['leafmachine']['landmark_detector']['do_save_final_images']:
            validate_dir(self.landmarks_whole_leaves_overlay_final)
            validate_dir(self.landmarks_partial_leaves_overlay_final)


        
            




    def __add_time_to_existing_project_dir(self) -> None:
        path = pathlib.Path(self.dir_project)
        if path.exists():
            now = get_datetime()
            path = path.with_name(path.name + "_" + now)
            self.run_name = path.name
            path.mkdir()
            self.dir_project = path
        else:
            path.mkdir()
            self.dir_project = path
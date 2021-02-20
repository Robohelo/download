
set(BUILD_SHARED_LIBS "ON")

set(CMAKE_BINARY_DIR "/tmp/build_opencv/opencv/build")

set(CMAKE_INSTALL_PREFIX "/usr/local")

set(OpenCV_SOURCE_DIR "/tmp/build_opencv/opencv")

set(OPENCV_PC_FILE_NAME "opencv4.pc")

set(OPENCV_VERSION_PLAIN "4.4.0")

set(OPENCV_LIB_INSTALL_PATH "lib")

set(OPENCV_INCLUDE_INSTALL_PATH "include/opencv4")

set(OPENCV_3P_LIB_INSTALL_PATH "lib/opencv4/3rdparty")

set(_modules "opencv_gapi;opencv_stitching;opencv_alphamat;opencv_aruco;opencv_bgsegm;opencv_bioinspired;opencv_ccalib;opencv_cudabgsegm;opencv_cudafeatures2d;opencv_cudaobjdetect;opencv_cudastereo;opencv_dnn_objdetect;opencv_dnn_superres;opencv_dpm;opencv_highgui;opencv_face;opencv_freetype;opencv_fuzzy;opencv_hdf;opencv_hfs;opencv_img_hash;opencv_intensity_transform;opencv_line_descriptor;opencv_quality;opencv_rapid;opencv_reg;opencv_rgbd;opencv_saliency;opencv_stereo;opencv_structured_light;opencv_phase_unwrapping;opencv_superres;opencv_cudacodec;opencv_surface_matching;opencv_tracking;opencv_datasets;opencv_text;opencv_dnn;opencv_plot;opencv_videostab;opencv_cudaoptflow;opencv_optflow;opencv_cudalegacy;opencv_videoio;opencv_cudawarping;opencv_xfeatures2d;opencv_shape;opencv_ml;opencv_ximgproc;opencv_video;opencv_xobjdetect;opencv_objdetect;opencv_calib3d;opencv_imgcodecs;opencv_features2d;opencv_flann;opencv_xphoto;opencv_photo;opencv_cudaimgproc;opencv_cudafilters;opencv_imgproc;opencv_cudaarithm;opencv_core;opencv_cudev")

set(_extra "m;pthread;cudart_static;-lpthread;dl;rt;nppc;nppial;nppicc;nppicom;nppidei;nppif;nppig;nppim;nppist;nppisu;nppitc;npps;cublas;cudnn;cufft;-L/usr/local/cuda/lib64;-L/usr/lib/aarch64-linux-gnu")

set(_3rdparty "")

set(TARGET_LOCATION_opencv_gapi "/tmp/build_opencv/opencv/build/lib/libopencv_gapi.so.4.4.0")

set(TARGET_LOCATION_opencv_stitching "/tmp/build_opencv/opencv/build/lib/libopencv_stitching.so.4.4.0")

set(TARGET_LOCATION_opencv_alphamat "/tmp/build_opencv/opencv/build/lib/libopencv_alphamat.so.4.4.0")

set(TARGET_LOCATION_opencv_aruco "/tmp/build_opencv/opencv/build/lib/libopencv_aruco.so.4.4.0")

set(TARGET_LOCATION_opencv_bgsegm "/tmp/build_opencv/opencv/build/lib/libopencv_bgsegm.so.4.4.0")

set(TARGET_LOCATION_opencv_bioinspired "/tmp/build_opencv/opencv/build/lib/libopencv_bioinspired.so.4.4.0")

set(TARGET_LOCATION_opencv_ccalib "/tmp/build_opencv/opencv/build/lib/libopencv_ccalib.so.4.4.0")

set(TARGET_LOCATION_opencv_cudabgsegm "/tmp/build_opencv/opencv/build/lib/libopencv_cudabgsegm.so.4.4.0")

set(TARGET_LOCATION_opencv_cudafeatures2d "/tmp/build_opencv/opencv/build/lib/libopencv_cudafeatures2d.so.4.4.0")

set(TARGET_LOCATION_opencv_cudaobjdetect "/tmp/build_opencv/opencv/build/lib/libopencv_cudaobjdetect.so.4.4.0")

set(TARGET_LOCATION_opencv_cudastereo "/tmp/build_opencv/opencv/build/lib/libopencv_cudastereo.so.4.4.0")

set(TARGET_LOCATION_opencv_dnn_objdetect "/tmp/build_opencv/opencv/build/lib/libopencv_dnn_objdetect.so.4.4.0")

set(TARGET_LOCATION_opencv_dnn_superres "/tmp/build_opencv/opencv/build/lib/libopencv_dnn_superres.so.4.4.0")

set(TARGET_LOCATION_opencv_dpm "/tmp/build_opencv/opencv/build/lib/libopencv_dpm.so.4.4.0")

set(TARGET_LOCATION_opencv_highgui "/tmp/build_opencv/opencv/build/lib/libopencv_highgui.so.4.4.0")

set(TARGET_LOCATION_opencv_face "/tmp/build_opencv/opencv/build/lib/libopencv_face.so.4.4.0")

set(TARGET_LOCATION_opencv_freetype "/tmp/build_opencv/opencv/build/lib/libopencv_freetype.so.4.4.0")

set(TARGET_LOCATION_opencv_fuzzy "/tmp/build_opencv/opencv/build/lib/libopencv_fuzzy.so.4.4.0")

set(TARGET_LOCATION_opencv_hdf "/tmp/build_opencv/opencv/build/lib/libopencv_hdf.so.4.4.0")

set(TARGET_LOCATION_opencv_hfs "/tmp/build_opencv/opencv/build/lib/libopencv_hfs.so.4.4.0")

set(TARGET_LOCATION_opencv_img_hash "/tmp/build_opencv/opencv/build/lib/libopencv_img_hash.so.4.4.0")

set(TARGET_LOCATION_opencv_intensity_transform "/tmp/build_opencv/opencv/build/lib/libopencv_intensity_transform.so.4.4.0")

set(TARGET_LOCATION_opencv_line_descriptor "/tmp/build_opencv/opencv/build/lib/libopencv_line_descriptor.so.4.4.0")

set(TARGET_LOCATION_opencv_quality "/tmp/build_opencv/opencv/build/lib/libopencv_quality.so.4.4.0")

set(TARGET_LOCATION_opencv_rapid "/tmp/build_opencv/opencv/build/lib/libopencv_rapid.so.4.4.0")

set(TARGET_LOCATION_opencv_reg "/tmp/build_opencv/opencv/build/lib/libopencv_reg.so.4.4.0")

set(TARGET_LOCATION_opencv_rgbd "/tmp/build_opencv/opencv/build/lib/libopencv_rgbd.so.4.4.0")

set(TARGET_LOCATION_opencv_saliency "/tmp/build_opencv/opencv/build/lib/libopencv_saliency.so.4.4.0")

set(TARGET_LOCATION_opencv_stereo "/tmp/build_opencv/opencv/build/lib/libopencv_stereo.so.4.4.0")

set(TARGET_LOCATION_opencv_structured_light "/tmp/build_opencv/opencv/build/lib/libopencv_structured_light.so.4.4.0")

set(TARGET_LOCATION_opencv_phase_unwrapping "/tmp/build_opencv/opencv/build/lib/libopencv_phase_unwrapping.so.4.4.0")

set(TARGET_LOCATION_opencv_superres "/tmp/build_opencv/opencv/build/lib/libopencv_superres.so.4.4.0")

set(TARGET_LOCATION_opencv_cudacodec "/tmp/build_opencv/opencv/build/lib/libopencv_cudacodec.so.4.4.0")

set(TARGET_LOCATION_opencv_surface_matching "/tmp/build_opencv/opencv/build/lib/libopencv_surface_matching.so.4.4.0")

set(TARGET_LOCATION_opencv_tracking "/tmp/build_opencv/opencv/build/lib/libopencv_tracking.so.4.4.0")

set(TARGET_LOCATION_opencv_datasets "/tmp/build_opencv/opencv/build/lib/libopencv_datasets.so.4.4.0")

set(TARGET_LOCATION_opencv_text "/tmp/build_opencv/opencv/build/lib/libopencv_text.so.4.4.0")

set(TARGET_LOCATION_opencv_dnn "/tmp/build_opencv/opencv/build/lib/libopencv_dnn.so.4.4.0")

set(TARGET_LOCATION_opencv_plot "/tmp/build_opencv/opencv/build/lib/libopencv_plot.so.4.4.0")

set(TARGET_LOCATION_opencv_videostab "/tmp/build_opencv/opencv/build/lib/libopencv_videostab.so.4.4.0")

set(TARGET_LOCATION_opencv_cudaoptflow "/tmp/build_opencv/opencv/build/lib/libopencv_cudaoptflow.so.4.4.0")

set(TARGET_LOCATION_opencv_optflow "/tmp/build_opencv/opencv/build/lib/libopencv_optflow.so.4.4.0")

set(TARGET_LOCATION_opencv_cudalegacy "/tmp/build_opencv/opencv/build/lib/libopencv_cudalegacy.so.4.4.0")

set(TARGET_LOCATION_opencv_videoio "/tmp/build_opencv/opencv/build/lib/libopencv_videoio.so.4.4.0")

set(TARGET_LOCATION_opencv_cudawarping "/tmp/build_opencv/opencv/build/lib/libopencv_cudawarping.so.4.4.0")

set(TARGET_LOCATION_opencv_xfeatures2d "/tmp/build_opencv/opencv/build/lib/libopencv_xfeatures2d.so.4.4.0")

set(TARGET_LOCATION_opencv_shape "/tmp/build_opencv/opencv/build/lib/libopencv_shape.so.4.4.0")

set(TARGET_LOCATION_opencv_ml "/tmp/build_opencv/opencv/build/lib/libopencv_ml.so.4.4.0")

set(TARGET_LOCATION_opencv_ximgproc "/tmp/build_opencv/opencv/build/lib/libopencv_ximgproc.so.4.4.0")

set(TARGET_LOCATION_opencv_video "/tmp/build_opencv/opencv/build/lib/libopencv_video.so.4.4.0")

set(TARGET_LOCATION_opencv_xobjdetect "/tmp/build_opencv/opencv/build/lib/libopencv_xobjdetect.so.4.4.0")

set(TARGET_LOCATION_opencv_objdetect "/tmp/build_opencv/opencv/build/lib/libopencv_objdetect.so.4.4.0")

set(TARGET_LOCATION_opencv_calib3d "/tmp/build_opencv/opencv/build/lib/libopencv_calib3d.so.4.4.0")

set(TARGET_LOCATION_opencv_imgcodecs "/tmp/build_opencv/opencv/build/lib/libopencv_imgcodecs.so.4.4.0")

set(TARGET_LOCATION_opencv_features2d "/tmp/build_opencv/opencv/build/lib/libopencv_features2d.so.4.4.0")

set(TARGET_LOCATION_opencv_flann "/tmp/build_opencv/opencv/build/lib/libopencv_flann.so.4.4.0")

set(TARGET_LOCATION_opencv_xphoto "/tmp/build_opencv/opencv/build/lib/libopencv_xphoto.so.4.4.0")

set(TARGET_LOCATION_opencv_photo "/tmp/build_opencv/opencv/build/lib/libopencv_photo.so.4.4.0")

set(TARGET_LOCATION_opencv_cudaimgproc "/tmp/build_opencv/opencv/build/lib/libopencv_cudaimgproc.so.4.4.0")

set(TARGET_LOCATION_opencv_cudafilters "/tmp/build_opencv/opencv/build/lib/libopencv_cudafilters.so.4.4.0")

set(TARGET_LOCATION_opencv_imgproc "/tmp/build_opencv/opencv/build/lib/libopencv_imgproc.so.4.4.0")

set(TARGET_LOCATION_opencv_cudaarithm "/tmp/build_opencv/opencv/build/lib/libopencv_cudaarithm.so.4.4.0")

set(TARGET_LOCATION_opencv_core "/tmp/build_opencv/opencv/build/lib/libopencv_core.so.4.4.0")

set(TARGET_LOCATION_opencv_cudev "/tmp/build_opencv/opencv/build/lib/libopencv_cudev.so.4.4.0")

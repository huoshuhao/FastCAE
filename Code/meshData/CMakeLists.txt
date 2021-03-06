CMAKE_MINIMUM_REQUIRED(VERSION 3.15.0 FATAL_ERROR)
SET(PROJECTNAME MeshData)
PROJECT(${PROJECTNAME})
ADD_DEFINITIONS("-DMESHDATA_API")
SET(CMAKE_CXX_STANDARD 11)

IF(NOT DEFINED Qt5_DIR)
	SET(Qt5_DIR "Qt5_DIR-NOTFOUND" CACHE PATH "Qt5_DIR")
ENDIF()
IF(NOT DEFINED FASTCAE_VTK_INCLUDE)
	SET(FASTCAE_VTK_INCLUDE "FASTCAE_VTK_INCLUDE-NOTFOUND" CACHE PATH "FASTCAE_VTK_INCLUDE")		
ENDIF()
IF(FASTCAE_VTK_INCLUDE STREQUAL "FASTCAE_VTK_INCLUDE-NOTFOUND")		
	MESSAGE(SEND_ERROR "FASTCAE_VTK_INCLUDE is null, please specified VTK include directory!~")
ENDIF()
IF(Qt5_DIR STREQUAL "Qt5_DIR-NOTFOUND")		
	MESSAGE(SEND_ERROR "Qt5_DIR is null, please specified Qt5Config.cmake location!~")
ENDIF()

IF(CMAKE_SYSTEM_NAME MATCHES "Linux")
	IF(NOT DEFINED FASTCAE_VTK_SO_DIR)
		SET(FASTCAE_VTK_SO_DIR "FASTCAE_VTK_SO_DIR-NOTFOUND" CACHE PATH "FASTCAE_VTK_SO_DIR")			
	ENDIF()	
	
	IF(FASTCAE_VTK_SO_DIR STREQUAL "FASTCAE_VTK_SO_DIR-NOTFOUND")		
		MESSAGE(FATAL_ERROR "FASTCAE_VTK_SO_DIR is null, please specified VTK so directory!~")
	ENDIF()
	SET(CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG ${CMAKE_CURRENT_SOURCE_DIR}/../../output/bin)
	SET(CMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}/../../output/bin)		
ELSEIF(CMAKE_SYSTEM_NAME MATCHES "Windows")
	IF(NOT DEFINED FASTCAE_VTK_LIBDIR)
		SET(FASTCAE_VTK_LIBDIR "FASTCAE_VTK_LIBDIR-NOTFOUND" CACHE PATH "FASTCAE_VTK_LIBDIR")			
	ENDIF()
	IF(NOT DEFINED FASTCAE_VTK_LIBDDIR)
		SET(FASTCAE_VTK_LIBDDIR "FASTCAE_VTK_LIBDDIR-NOTFOUND" CACHE PATH "FASTCAE_VTK_LIBDDIR")			
	ENDIF()
	IF(NOT DEFINED FASTCAE_VTK_BINDIR)
		SET(FASTCAE_VTK_BINDIR "FASTCAE_VTK_BINDIR-NOTFOUND" CACHE PATH "FASTCAE_VTK_BINDIR")			
	ENDIF()
	IF(NOT DEFINED FASTCAE_VTK_BINDDIR)
		SET(FASTCAE_VTK_BINDDIR "FASTCAE_VTK_BINDDIR-NOTFOUND" CACHE PATH "FASTCAE_VTK_BINDDIR")			
	ENDIF()
	
	IF(FASTCAE_VTK_LIBDIR STREQUAL "FASTCAE_VTK_LIBDIR-NOTFOUND")		
		MESSAGE(SEND_ERROR "FASTCAE_VTK_LIBDIR is null, please specified VTK lib directory!~")
	ENDIF()
	IF(FASTCAE_VTK_LIBDDIR STREQUAL "FASTCAE_VTK_LIBDDIR-NOTFOUND")		
		MESSAGE(SEND_ERROR "FASTCAE_VTK_LIBDDIR is null, please specified VTK libd directory!~")
	ENDIF()
	IF(FASTCAE_VTK_BINDIR STREQUAL "FASTCAE_VTK_BINDIR-NOTFOUND")		
		MESSAGE(SEND_ERROR "FASTCAE_VTK_BINDIR is null, please specified VTK bin directory!~")
	ENDIF()
	IF(FASTCAE_VTK_BINDDIR STREQUAL "FASTCAE_VTK_BINDDIR-NOTFOUND")		
		MESSAGE(FATAL_ERROR "FASTCAE_VTK_BINDDIR is null, please specified VTK bind directory!~")
	ENDIF()	
	SET(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG ${CMAKE_CURRENT_SOURCE_DIR}/../../output/bin_d)    
	SET(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}/../../output/bin) 
	SET(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_CURRENT_SOURCE_DIR}/../../output/bin_d)   
	SET(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}/../../output/bin) 	
ENDIF()

FILE(GLOB SRC_H_FILES "*.h")
FILE(GLOB SRC_CPP_FILES "*.cpp")
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/.. 
					${FASTCAE_VTK_INCLUDE})

FIND_PACKAGE(Qt5 COMPONENTS Widgets Xml REQUIRED)
ADD_LIBRARY(${PROJECTNAME} SHARED ${SRC_H_FILES} ${SRC_CPP_FILES})
TARGET_LINK_LIBRARIES(${PROJECTNAME} Qt5::Xml Qt5::Widgets)
IF(CMAKE_SYSTEM_NAME MATCHES "Linux")	
	IF(NOT DEFINED FASTCAE_VTK_SOS_0)
		FILE(GLOB FASTCAE_VTK_SOS_0 "${FASTCAE_VTK_SO_DIR}/*.so")
	ENDIF()
	
	FOREACH(FASTCAE_VTK_SO_0 ${FASTCAE_VTK_SOS_0})
		TARGET_LINK_LIBRARIES(${PROJECTNAME} ${FASTCAE_VTK_SO_0})
	ENDFOREACH()
	TARGET_LINK_LIBRARIES(${PROJECTNAME} debug "${CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG}/libDataProperty${CMAKE_DEBUG_POSTFIX}.so" optimized "${CMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE}/libDataProperty${CMAKE_RELEASE_POSTFIX}.so")
ELSEIF(CMAKE_SYSTEM_NAME MATCHES "Windows")	
	IF(NOT DEFINED FASTCAE_VTK_LIBDS)
		FILE(GLOB FASTCAE_VTK_LIBDS "${FASTCAE_VTK_LIBDDIR}/*.lib")
	ENDIF()
	IF(NOT DEFINED FASTCAE_VTK_LIBS)
		FILE(GLOB FASTCAE_VTK_LIBS "${FASTCAE_VTK_LIBDIR}/*.lib")
	ENDIF()
	
	FOREACH(FASTCAE_VTK_LIBD ${FASTCAE_VTK_LIBDS})
		TARGET_LINK_LIBRARIES(${PROJECTNAME} debug ${FASTCAE_VTK_LIBD})
	ENDFOREACH()	
	FOREACH(FASTCAE_VTK_LIB ${FASTCAE_VTK_LIBS})
		TARGET_LINK_LIBRARIES(${PROJECTNAME} optimized ${FASTCAE_VTK_LIB})
	ENDFOREACH()	
	TARGET_LINK_LIBRARIES(${PROJECTNAME} debug "${CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG}/DataProperty${CMAKE_DEBUG_POSTFIX}.lib" optimized "${CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE}/DataProperty${CMAKE_RELEASE_POSTFIX}.lib")
ENDIF()

IF(TARGET SolutionDataIO)	
	ADD_DEPENDENCIES(${PROJECTNAME} DataProperty)
ENDIF()
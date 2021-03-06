#ifndef PREPAREDET_H_INCLUDED
#define PREPAREDET_H_INCLUDED

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/ml/ml.hpp>
#include <string.h>
#include "featureExtraction.h"


void createDETfile();
std::vector<float> testQuantitativDET_pos(bool first);
std::vector<long double> testQuantitativDET_neg(bool first);

#endif
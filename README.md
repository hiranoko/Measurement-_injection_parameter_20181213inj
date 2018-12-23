Beam study at 20181213
====

## Install

���ɂ���܂���

## Requirement

pip install pyepics

pip install numpy

## Usage

Provide the optimization of injection parameters at KEK-PF.

�ȉ��̊֐����Ăяo���Ƒ���ƍœK�������s�\�ł��B

# vim main.py
import roboter.controller.conversation
import measurement_obj.objectivefunction.parameters.conj_opt

### ����ɂ���

1. parameters.py

This moduel have function getting file name and recoed list, return list value.
And returns value using pyepics lib from file containing record name.
../parameters_list
 |- kicker_parameters
 |- libera_arm
 |- libera_tbt_H
 |- libera_tbt_V

2. measurement_obj.py

This moduel have function getting objective value and scannning knob parameters.
Scanning parameters are Delay time [nsec] and Angle [mrad] at downstream Kickers.

### �œK���ɂ���

1. conj_opt.py

The function of this module is the acquisition of slope and comparison of values.

# Setting
(�I�v�V����: �ۑ�����f�B���N�g����t���[�p�����^�[��ύX����ꍇ�́A�ȉ��̒l������������B)
'20181213_inj/code/data/'
'20181213_inj/code/parameters/'

## Author

Hirano Kota

hiranoko@post.kek.jp


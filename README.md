Beam study at 20181213
====

## Install

特にありません

## Requirement

pip install pyepics

pip install numpy

## Usage

Provide the optimization of injection parameters at KEK-PF.

以下の関数を呼び出すと測定と最適化が実行可能です。

# vim main.py
import roboter.controller.conversation
import measurement_obj.objectivefunction.parameters.conj_opt

### 測定について

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

### 最適化について

1. conj_opt.py

The function of this module is the acquisition of slope and comparison of values.

# Setting
(オプション: 保存するディレクトリやフリーパラメターを変更する場合は、以下の値を書き換える。)
'20181213_inj/code/data/'
'20181213_inj/code/parameters/'

## Author

Hirano Kota

hiranoko@post.kek.jp


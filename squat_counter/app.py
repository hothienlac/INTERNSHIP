import argparse

from count import Count
from train import Train
from process_data import ProcessData



def main(args):
    
    actions_dictionary = {
        'count': Count,
        'train': Train,
        'process_data': ProcessData,
    }

    action = actions_dictionary[args.action](args)

    action.run()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Squat Counter',
        description='This program is used to count squat exercise',
    )
    parser.add_argument(
        'action',
        choices=['count', 'train', 'process_data'],
    )
    parser.add_argument(
        '-v', '--video',
        type=str,
        help='Path to video to count.',
    )
    parser.add_argument(
        '-m', '--model',
        type=str,
        choices=['random_forest', 'gaussian_naive_bayes', 'deep_neural_network'],
        default='random_forest',
        help='Model to classify posture. "random_forest" as default',
    )
    parser.add_argument(
        '-mp', '--model-path',
        type=str,
        help='Model path. ./models/\{modelname\}.model by default',
    )
    parser.add_argument(
        '-mo', '--model-output',
        type=str,
        help='Model output path. ./models/\{modelname\}.model by default',
    )
    parser.add_argument(
        '-vo', '--video-output',
        type=str,
        help='Output path. Same directory by default, and "_count_squat.mp4" postfix',
    )
    parser.add_argument(
        '-d', '--data',
        type=str,
        default='./data/data.csv',
        help='Training data. Use relative path. "./data/data.csv" as default',
    )
    parser.add_argument(
        '-di', '--data-input',
        type=str,
        default='./data/combined',
        help='Output relative path. Contain at teast 3 sub directory, including ["sit", "middle", "stand"]. "./data/combined" as default',
    )
    parser.add_argument(
        '-do', '--data-output',
        type=str,
        default='./data/data.csv',
        help='Output relative path. "./data/data.csv" as default',
    )

    args = parser.parse_args()

    main(args)

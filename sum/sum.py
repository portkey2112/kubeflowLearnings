import kfp
from kfp.components import func_to_container_op, InputPath, OutputPath

@func_to_container_op
def sum(a: int, b: int, output_text_path: OutputPath(str)):
    res = a + b
    with open(output_text_path, 'w') as writer:
        writer.write(f'Given nos are {a} and {b}. The sum is {res}')

@func_to_container_op
def print_sum_from_file(sum_path: InputPath()):
    with open(sum_path, 'r') as reader:
        for line in reader:
            print(line)

def sum_pipeline(a: int, b: int):
    sum_task = sum(a,b)
    print_sum_from_file(sum_task.output)

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(sum_pipeline, 'sum_pipeline.yaml')
    #kfp.Client().create_run_from_pipeline_func(sum_pipeline, arguments={})
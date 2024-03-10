from f.gitter.prepare_q import f as prepare_q
from f.gitter.git_pull import f as git_pull
from f.gitter.git_status import f as git_status
from f.directory.to_dependency_graph import f as to_dependency_graph
from f.gitter.f_generic import f as f_X
from os.path import exists

def _f(dependency_graph, committable_filepaths):
  filepaths = sorted(committable_filepaths)
  for set_length in range(10):
    for _committable_filepath in filepaths:
      if _committable_filepath.endswith('.py'):
        if exists(_committable_filepath):
          joint_set = (
            dependency_graph[_committable_filepath] &
            set(committable_filepaths)
          )
          if len(joint_set) == set_length:
            print('!20')
            print(f'set(committable_filepaths): {set(committable_filepaths)}')
            print(f'_committable_filepath: {_committable_filepath}')
            print(': '.join([
              f'dependency_graph[{_committable_filepath}]',
              f'{dependency_graph[_committable_filepath]}'
            ]))
            print(f'joint_set:      {joint_set}')
            print(f'len(joint_set): {len(joint_set)}')
            print(f'set_length:     {set_length}')
            return _committable_filepath
        else:
          print(f'25: _committable_filepath: {_committable_filepath}')
          return _committable_filepath
      else:
        print('!28')
        return _committable_filepath

  print('!26')
  print(filepaths)
  return filepaths[0]

# main
def f(ask):
  git_pull()
  status_result = git_status()
  q = prepare_q(status_result)
  _committable_filepaths = ['./'+_.split(' ')[-1] for _ in q]
  _dg = to_dependency_graph(_committable_filepaths)
  from hak.file.save import f as save
  from hak.dict.to_str import f as dict_to_str
  save('dg.txt', dict_to_str(_dg)+'\n')
  priority_committable = _f(_dg, _committable_filepaths)
  code_to_word = {' M': 'Updated', '??': 'Added', ' D': 'Removed'}
  _d = {f'./{_[3:]}': _[:2] for _ in q}
  _action = code_to_word[_d[priority_committable]]
  _ask = False if _action == 'Removed' else ask
  f_X(priority_committable, _action, _ask)
  if len(q) > 1: f(ask)

t = lambda: 1

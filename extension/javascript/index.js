// https://github.com/extrabacon/python-shell
const { PythonShell } = require('python-shell');

const options = {
    mode: 'text',
    pythonPath: '',
    pythonOptions: ['-u'],
    scriptPath: '',
    args: ['value1', 'value2', 'value3']
};

PythonShell.run('test.py', options, function(err, results) {
    if (err) throw err;

    console.log('result: %j', results);
    const arr = getArr(results[0]);
    console.log(arr[0], arr[1])
})

getArr = str => {
    res = null;
    if (str) {
        str = str.replace(/'/g, '"');
        try {
            res = JSON.parse(str);
        } catch(err) {
            console.log("err : ", err)
        }
    }

    return res;
}
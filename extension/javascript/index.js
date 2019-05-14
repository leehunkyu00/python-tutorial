const ps = require('python-shell').PythonShell;

const options = {
    mode: 'text',
    pythonPath: '',
    pythonOptions: ['-u'],
    scriptPath: '',
    args: ['value1', 'value2', 'value3']
};

ps.run('test.py', options, function(err, results) {
    if (err) throw err;

    console.log('result: %j', results);
})

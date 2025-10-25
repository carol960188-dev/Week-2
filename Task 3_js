function func3(index){ // index 是 0-based
  const numbers = [25, 23, 20, 21, 23, 21, 18, 19, 21, 19, 16, 17];
  const pattern = [-2, -3, 1, 2];
  const predict = [...numbers];

  while (predict.length <= index) {
    const step = pattern[(predict.length - 1) % pattern.length];
    predict.push(predict[predict.length - 1] + step);
  }

  console.log(predict[index]);
}

func3(1); // print 23
func3(5); // print 21
func3(10); // print 16
func3(30); // print 6

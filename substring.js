function slinkysubstring (str1, str2) {
  let sub = '';
  for (var startpos = 0; startpos < str1.length; startpos++) {
    // if the current sub is larger than the characters left we know we have the
    // longest substring
    if (str1.length - startpos < sub.length) break;
    for (var startpos2 = 0; startpos2 < str2.length; startpos2++) {
      if (str2.length - startpos2 < sub.length) break;

      let length = sub.length + 1;
      while (str1.substring(startpos, startpos + length) === str2.substring(startpos2, startpos2 + length)) {
        length++;
        if (length > str2.length) break;
      }
      // We know the loop incremented the length one extra time before it broke
      // so we decrement it.
      length--;
      if (sub.length < length) {
        sub = str1.substring(startpos, startpos + length);
        startpos += sub.length;
      }
    }
  }
  return sub;
}

console.log('Longest Substring: ' + slinkysubstring('ultrulta', 'sultiulta'));
console.log('Longest Substring: ' + slinkysubstring('dignified', 'unified'));
console.log('Longest Substring: ' + slinkysubstring('unified', 'unified'));
console.log('Longest Substring: ' + slinkysubstring('mat', 'sring'));
console.log('Longest Substring: ' + slinkysubstring('swarray', 'array'));

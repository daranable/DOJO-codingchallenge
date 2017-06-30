function longestsubstring (str1, str2) {
  let subs = {};
  let sublen = Math.round(str1.length / 2);
  console.log(sublen);

  while (true) {
    for (let i = 0; i <= str1.length - sublen; i++) {
      let sub = str1.substring(i, i + sublen);
      for (let i = 0; i <= str2.length - sublen; i++) {
        let sub2 = str2.substring(i, i + sublen);
        if (sub === sub2) {
          console.log('MATCH', sub, sub2, sublen);
          if (!subs[sublen]) subs[sublen] = [];
          subs[sublen].push(sub);
        }
      }
    }
    if (!subs[sublen] & typeof subs[sublen - 1] === 'object') {
      return subs[sublen - 1];
    } if (!subs[sublen]) {
      subs[sublen] = -1;
      sublen--;
    } else if (typeof subs[sublen] === 'object' & subs[sublen + 1] === -1) {
      return subs[sublen];
    } else {
      sublen++;
    }
  }
}

console.log('Longest Substring: ' + longestsubstring('catapults', 'ultrasound'));
console.log('Longest Substring: ' + longestsubstring('dignified', 'unified'));

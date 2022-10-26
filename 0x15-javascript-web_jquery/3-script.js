#!/usr/bin/node
const $ = window.$;
$('DIV#red_header').click(function () {
  $('HEADER').addClass('red');
});

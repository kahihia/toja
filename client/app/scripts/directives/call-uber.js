'use strict';

/**
 * @ngdoc directive
 * @name clientApp.directive:callUber
 * @description
 * # callUber
 */
angular.module('clientApp')
  .directive('callUber', function ($mdDialog) {
    return {
      templateUrl: 'views/directives/call-uber.html',
      restrict: 'E',
      replace: true,
      link: function postLink(scope) {
        scope.callUber = function(event) {
          var confirm = $mdDialog.confirm()
            .title('Open in Uber?')
            //.textContent('All of the banks have agreed to forgive you your debts.')
            .ariaLabel('Uber')
            .targetEvent(event)
            .ok('OK')
            .cancel('Cancel');
          $mdDialog.show(confirm).then(function onOk() {
            console.debug('Open in Uber');
          }, function onCancel() {
            console.debug('Cancel pressed');
          });
        };
      }
    };
  });

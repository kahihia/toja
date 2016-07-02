'use strict';

/**
 * @ngdoc function
 * @name clientApp.controller:ListingDetailCtrl
 * @description
 * # ListingDetailCtrl
 * Controller of the clientApp
 */
angular.module('clientApp')
.config(function($stateProvider) {

  $stateProvider
  .state('listing-detail', {
    url: '/detail/:placeId',
    templateUrl: 'views/listing-detail.html',
    controller: 'ListingDetailCtrl as ctrl'
  });

})
.controller('ListingDetailCtrl', function () {
  this.map = { center: { latitude: 45, longitude: -73 }, zoom: 8 };
});

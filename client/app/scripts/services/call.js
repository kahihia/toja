'use strict';

/**
 * @ngdoc service
 * @name clientApp.Call
 * @description
 * # Call
 * Service in the clientApp.
 */
angular.module('clientApp')
  .service('Call', function ($resource, API_END_POINT) {
    return $resource(API_END_POINT + '/call/:id', {}, {
      get: {
        method: 'GET',
        transformResponse: function(data) {
          var record = angular.fromJson(data);

          if (!record) {
            return {};
          }

          // TODO: return Array of images from server side
          // instead of String
          if (angular.isObject(record)) {
            if (record.images && record.images !== '') {
              record.images = JSON.parse(record.images);
            }
            return record;
          } else {
            return record;
          }
        }
      }
    });
  });

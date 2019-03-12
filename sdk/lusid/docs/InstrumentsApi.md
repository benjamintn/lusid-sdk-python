# lusid.InstrumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_instrument**](InstrumentsApi.md#delete_instrument) | **DELETE** /api/instruments/{identifierType}/{identifier} | Delete instrument
[**find_instruments**](InstrumentsApi.md#find_instruments) | **POST** /api/instruments/$find | Search instrument definition
[**get_instrument**](InstrumentsApi.md#get_instrument) | **GET** /api/instruments/{identifierType}/{identifier} | Get instrument definition
[**get_instrument_identifiers**](InstrumentsApi.md#get_instrument_identifiers) | **GET** /api/instruments/identifiers | Get allowable instrument identifiers
[**get_instruments**](InstrumentsApi.md#get_instruments) | **POST** /api/instruments/$get | Get instrument definition
[**list_instruments**](InstrumentsApi.md#list_instruments) | **GET** /api/instruments | Get all of the currently mastered instruments in LUSID
[**match_instruments**](InstrumentsApi.md#match_instruments) | **POST** /api/instruments/$match | Find externally mastered instruments
[**update_instrument_identifier**](InstrumentsApi.md#update_instrument_identifier) | **POST** /api/instruments/{identifierType}/{identifier} | Update instrument identifier
[**upsert_instruments**](InstrumentsApi.md#upsert_instruments) | **POST** /api/instruments | Upsert instruments
[**upsert_instruments_properties**](InstrumentsApi.md#upsert_instruments_properties) | **POST** /api/instruments/$upsertproperties | Upsert instrument properties


# **delete_instrument**
> DeleteInstrumentResponse delete_instrument(identifier_type, identifier)

Delete instrument

Attempt to delete one or more \"client\" instruments.    The response will include those instruments that could not be deleted (as well as any available details).                It is important to always check the 'Failed' set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
identifier_type = 'identifier_type_example' # str | The type of identifier being supplied
identifier = 'identifier_example' # str | The instrument identifier

try:
    # Delete instrument
    api_response = api_instance.delete_instrument(identifier_type, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->delete_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The type of identifier being supplied | 
 **identifier** | **str**| The instrument identifier | 

### Return type

[**DeleteInstrumentResponse**](DeleteInstrumentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_instruments**
> ResourceListOfInstrument find_instruments(effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys, model_property=model_property)

Search instrument definition

Get a collection of instruments by a set of identifiers. Optionally, it is possible to decorate each instrument with specified property data.

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the query (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the query (optional)
instrument_property_keys = ['instrument_property_keys_example'] # list[str] | Optional. Keys of the properties to be decorated on to the instrument (optional)
model_property = NULL # list[ModelProperty] | The list of market aliases (e.g ISIN, Ticker) to find instruments by. (optional)

try:
    # Search instrument definition
    api_response = api_instance.find_instruments(effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys, model_property=model_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->find_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **datetime**| Optional. The effective date of the query | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the query | [optional] 
 **instrument_property_keys** | [**list[str]**](str.md)| Optional. Keys of the properties to be decorated on to the instrument | [optional] 
 **model_property** | [**list[ModelProperty]**](list.md)| The list of market aliases (e.g ISIN, Ticker) to find instruments by. | [optional] 

### Return type

[**ResourceListOfInstrument**](ResourceListOfInstrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument**
> Instrument get_instrument(identifier_type, identifier, effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys)

Get instrument definition

Get an individual instrument by the one of its unique instrument identifiers. Optionally, it is possible to decorate each instrument with specified property data.

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
identifier_type = 'identifier_type_example' # str | The type of identifier being supplied
identifier = 'identifier_example' # str | The identifier of the requested instrument
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the query (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date of the query (optional)
instrument_property_keys = ['instrument_property_keys_example'] # list[str] | Optional. Keys of the properties to be decorated on to the instrument (optional)

try:
    # Get instrument definition
    api_response = api_instance.get_instrument(identifier_type, identifier, effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->get_instrument: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The type of identifier being supplied | 
 **identifier** | **str**| The identifier of the requested instrument | 
 **effective_at** | **datetime**| Optional. The effective date of the query | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date of the query | [optional] 
 **instrument_property_keys** | [**list[str]**](str.md)| Optional. Keys of the properties to be decorated on to the instrument | [optional] 

### Return type

[**Instrument**](Instrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instrument_identifiers**
> ResourceListOfString get_instrument_identifiers()

Get allowable instrument identifiers

Gets the set of identifiers that have been configured as unique identifiers for instruments.     Only CodeTypes returned from this end point can be used as identifiers for instruments.

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))

try:
    # Get allowable instrument identifiers
    api_response = api_instance.get_instrument_identifiers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->get_instrument_identifiers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfString**](ResourceListOfString.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instruments**
> GetInstrumentsResponse get_instruments(identifier_type=identifier_type, effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys, request_body=request_body)

Get instrument definition

Get a collection of instruments by a set of identifiers. Optionally, it is possible to decorate each instrument with specified property data.

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
identifier_type = 'identifier_type_example' # str | The type of identifiers being supplied (optional)
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the request (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The as at date of the request (optional)
instrument_property_keys = ['instrument_property_keys_example'] # list[str] | Optional. Keys of the properties to be decorated on to the instrument (optional)
request_body = NULL # list[str] | The identifiers of the instruments to get (optional)

try:
    # Get instrument definition
    api_response = api_instance.get_instruments(identifier_type=identifier_type, effective_at=effective_at, as_at=as_at, instrument_property_keys=instrument_property_keys, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->get_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The type of identifiers being supplied | [optional] 
 **effective_at** | **datetime**| Optional. The effective date of the request | [optional] 
 **as_at** | **datetime**| Optional. The as at date of the request | [optional] 
 **instrument_property_keys** | [**list[str]**](str.md)| Optional. Keys of the properties to be decorated on to the instrument | [optional] 
 **request_body** | [**list[str]**](list.md)| The identifiers of the instruments to get | [optional] 

### Return type

[**GetInstrumentsResponse**](GetInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instruments**
> ResourceListOfInstrument list_instruments(as_at=as_at, effective_at=effective_at, sort_by=sort_by, start=start, limit=limit, filter=filter, instrument_property_keys=instrument_property_keys)

Get all of the currently mastered instruments in LUSID

Lists all instruments that have been mastered within LUSID.

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt time (optional)
effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The effective date of the query (optional)
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many (optional)
filter = 'State eq 'Active'' # str | Optional. Expression to filter the result set - the default filter returns only instruments in the Active state (optional) (default to 'State eq 'Active'')
instrument_property_keys = ['instrument_property_keys_example'] # list[str] | Optional. Keys of the properties to be decorated on to the instrument (optional)

try:
    # Get all of the currently mastered instruments in LUSID
    api_response = api_instance.list_instruments(as_at=as_at, effective_at=effective_at, sort_by=sort_by, start=start, limit=limit, filter=filter, instrument_property_keys=instrument_property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->list_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The AsAt time | [optional] 
 **effective_at** | **datetime**| Optional. The effective date of the query | [optional] 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set - the default filter returns only instruments in the Active state | [optional] [default to &#39;State eq &#39;Active&#39;&#39;]
 **instrument_property_keys** | [**list[str]**](str.md)| Optional. Keys of the properties to be decorated on to the instrument | [optional] 

### Return type

[**ResourceListOfInstrument**](ResourceListOfInstrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_instruments**
> MatchInstrumentsResponse match_instruments(identifier_type=identifier_type, request_body=request_body)

Find externally mastered instruments

Search for a set of instruments from an external instrument mastering service

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
identifier_type = 'identifier_type_example' # str | The type of identifiers being supplied (optional)
request_body = NULL # list[str] | The identifiers of the instruments to get (optional)

try:
    # Find externally mastered instruments
    api_response = api_instance.match_instruments(identifier_type=identifier_type, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->match_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The type of identifiers being supplied | [optional] 
 **request_body** | [**list[str]**](list.md)| The identifiers of the instruments to get | [optional] 

### Return type

[**MatchInstrumentsResponse**](MatchInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instrument_identifier**
> Instrument update_instrument_identifier(identifier_type, identifier, update_instrument_identifier_request=update_instrument_identifier_request)

Update instrument identifier

Adds, updates, or removes an identifier on an instrument

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
identifier_type = 'identifier_type_example' # str | The type of identifier being supplied
identifier = 'identifier_example' # str | The instrument identifier
update_instrument_identifier_request = lusid.UpdateInstrumentIdentifierRequest() # UpdateInstrumentIdentifierRequest | The identifier to add, update, or remove (optional)

try:
    # Update instrument identifier
    api_response = api_instance.update_instrument_identifier(identifier_type, identifier, update_instrument_identifier_request=update_instrument_identifier_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->update_instrument_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_type** | **str**| The type of identifier being supplied | 
 **identifier** | **str**| The instrument identifier | 
 **update_instrument_identifier_request** | [**UpdateInstrumentIdentifierRequest**](UpdateInstrumentIdentifierRequest.md)| The identifier to add, update, or remove | [optional] 

### Return type

[**Instrument**](Instrument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instruments**
> UpsertInstrumentsResponse upsert_instruments(request_body=request_body)

Upsert instruments

Attempt to master one or more instruments in LUSID's instrument master. Each instrument is keyed by some unique key. This key is unimportant, and serves only as a method to identify created instruments in the response.    The response will return both the collection of successfully created instruments, as well as those that were rejected and why their creation failed. They will be keyed against the key supplied in the  request.                It is important to always check the 'Failed' set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
request_body = {'key': lusid.InstrumentDefinition()} # dict(str, InstrumentDefinition) | The instrument definitions (optional)

try:
    # Upsert instruments
    api_response = api_instance.upsert_instruments(request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->upsert_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, InstrumentDefinition)**](InstrumentDefinition.md)| The instrument definitions | [optional] 

### Return type

[**UpsertInstrumentsResponse**](UpsertInstrumentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_instruments_properties**
> UpsertInstrumentPropertiesResponse upsert_instruments_properties(upsert_instrument_property_request=upsert_instrument_property_request)

Upsert instrument properties

Attempt to upsert property data for one or more instruments, properties, and effective dates.    The response will include the details of any failures that occurred during data storage.                It is important to always check the 'Failed' collection for any unsuccessful results.

### Example

* OAuth Authentication (oauth2): 
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = lusid.InstrumentsApi(lusid.ApiClient(configuration))
upsert_instrument_property_request = NULL # list[UpsertInstrumentPropertyRequest] | The instrument property data (optional)

try:
    # Upsert instrument properties
    api_response = api_instance.upsert_instruments_properties(upsert_instrument_property_request=upsert_instrument_property_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstrumentsApi->upsert_instruments_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_instrument_property_request** | [**list[UpsertInstrumentPropertyRequest]**](list.md)| The instrument property data | [optional] 

### Return type

[**UpsertInstrumentPropertiesResponse**](UpsertInstrumentPropertiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

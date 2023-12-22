# Methodology

#METHODOLOGY 
#LOGICFLAWS 
<hr>

1. Use a proxy to test data validation in both server and client side.
2. Enter unexpected values for an specific field or parameter.

Try to answer

-   Are there any limits that are imposed on the data?
-   What happens when you reach those limits?
-   Is any transformation or normalization being performed on your input?

3. Test for functionalities that may make assumptions about user behavior.
4. Try removing each parameter in turn and observing what effect this has on the response. You should make sure to:

-   Only remove one parameter at a time to ensure all relevant code paths are reached.
-   Try deleting the name of the parameter as well as the value. The server will typically handle both cases differently.
5.  Follow multi-stage processes through to completion. Sometimes tampering with a parameter in one step will have an effect on another step further along in the workflow.
6. Test multi-step process within the application to check if any step can be bypassed and break access control.
7. Identify if certain functionalities can be abused.
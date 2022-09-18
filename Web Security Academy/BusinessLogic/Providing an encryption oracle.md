# Providing an encryption oracle

#THEORY 
#LOGICFLAWS 
<hr>

The base scenario is as follows:
- User controllable input is encrypted by the application
- The encrypted data is then available to the user

(This allows an attacker to encrypt arbitrary data with the correct algorithm and asymmetric key)

And there's another functionality that provides the reverse function. This would tell an attacker the specified structure to craft an exploit.

The severity of an encryption oracle depends on what functionality also uses the same algorithm as the oracle.
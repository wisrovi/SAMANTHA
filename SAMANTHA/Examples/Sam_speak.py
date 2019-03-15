SAM = Sam_bot("SAMANTHA")
SAM.AprenderIdiomaEspañol()

voiceSAM = SpeakSAM()



while True:
    try:
        pregunta  = input("Dime algo: ")
        response = SAM.RespuestaBot(pregunta)
        voiceSAM.talking(response)

        print("SAM: " + str(response))

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

SAM.ExportTraining()